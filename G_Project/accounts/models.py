from django.db import models
from django.contrib.auth.models import User
from main_info.models import City, CityDistrict, Job
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

img_ex = ['jpg', 'jpeg', 'gif', 'png']


def uploader(instance, filename):
    name = list((str(filename).lower()).split('.'))
    # ex mean extension = img.extension
    for ex in img_ex:
        if ex in name:
            if ex != 'jpg':
                ex = 'jpg'
                return ex
            else:
                return ex


def herafi_id_card_img_uploader(instance, filename):
    img = uploader(instance, filename)
    if img is not None:
        return f"herafi_id_card/%s_%s.{img}" % (str(instance.id), instance.full_name)
    else:
        return False


def profile_img_uploader(instance, filename):
    img = uploader(instance, filename)
    if img is not None:
        return f"profile/%s_%s.%s" % (str(instance.id), instance.full_name, img)
    else:
        return False


class Profile(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    img_id_card = models.ImageField(upload_to=herafi_id_card_img_uploader, null=True, blank=True)
    profile_img = models.ImageField(upload_to=profile_img_uploader, null=True, blank=True)
    banned = models.BooleanField(default=False)
    gender = models.BooleanField(default=False,
                                 help_text='1(selected or True) = female, 0(not-selected or False)  = male')
    bonuses_points = models.BigIntegerField(default=0, null=True, blank=True)
    berth_date = models.DateField(null=True, blank=True)
    city_id = models.ForeignKey(City, default=2, on_delete=models.CASCADE, null=True, blank=True)
    account_type = models.ForeignKey('AccountType', default=1, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user_id=instance)


class AccountType(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    type = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)


class PreferredHerafies(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    client_profile_id = models.ForeignKey('Profile', on_delete=models.CASCADE)
    herafi_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        id = self.client_profile_id.user_id.id
        owner = self.client_profile_id.full_name
        herafi_id = self.herafi_id
        herafi_name = self.herafi_id.username
        data = f"{id} {owner} {herafi_id} {herafi_name}"
        return data

    def save(self, *args, **kwargs):
        fast_search = Profile.objects.get(user_id=self.herafi_id)
        print(str(fast_search.id)+str(self.client_profile_id.id))
        if fast_search.id == self.client_profile_id.id or fast_search.account_type == 2:
            return None
        else:
            super(PreferredHerafies, self).save(*args, **kwargs)


class HerafiInformation(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    views = models.IntegerField(null=True, blank=True, default=0)
    requests = models.IntegerField(null=True, blank=True, default=0)
    price_of_preview = models.DecimalField(max_digits=5, decimal_places=2, default=00.0)
    experiences = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    phone_number = models.CharField(max_length=11)
    bio = models.TextField(max_length=1000, null=True, blank=True)
    job_category = models.ForeignKey(Job, on_delete=models.DO_NOTHING, default=1)
    profile_id = models.OneToOneField('Profile', on_delete=models.CASCADE)
    stars = models.IntegerField(default=0, null=True, blank=True)
    people_rated = models.IntegerField(default=0, null=True, blank=True)
    percentage_ratings = models.FloatField(default=0.0, null=True, blank=True)

    @receiver(post_save, sender=Profile)
    def create_profile_herafi(sender, instance, created, **kwargs):
        id = instance.account_type.id
        if id == 2:
            if created:
                HerafiInformation.objects.create(profile_id=instance)

    def __str__(self):
        id = self.id
        profile = self.profile_id.full_name
        profile_id = self.profile_id
        return f"{id} {profile} id = {profile_id.id}"
