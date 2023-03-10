from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.reverse import reverse


from .models import (
                    Profile,
                    PreferredHerafies,
                    HerafiInformation,
)
from .models import profile_img_uploader


class CreateUserAPI(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    account_type = serializers.CharField(style={'input_type': 'text'})
    job_category = serializers.CharField(style={'input_type': int}, required=False)
    gender = serializers.BooleanField(style={'input_type': bool})
    full_name = serializers.CharField(source='User.first_name')

    class Meta:
        model = User
        fields = [
            'id',
            'full_name',
            'username',
            'password',
            'password2',
            'account_type',
            'gender',
            'job_category',
        ]

    def save(self):
        user = User(
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'password must match'})
        user.set_password(password)
        user.save()


class AutoUpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['full_name', 'first_name', 'last_name', 'account_type', 'gender']


class HerafiIfoAPI(serializers.ModelSerializer):
    url_edit = serializers.SerializerMethodField(read_only=True)
    percentage_ratings = serializers.FloatField(read_only=True)
    class Meta:
        model = HerafiInformation
        # fields = '__all__'
        exclude = ['id', 'job_category', 'profile_id', 'stars', 'people_rated']

    def get_url_edit(self, obj):
        return f"/accounts/herafi/info/{obj.pk}/"


class UpdateProfileAPI(serializers.ModelSerializer):

    class Meta:

        model = Profile
        fields = [
            'full_name',
            'first_name',
            'last_name',
            'profile_img',
            'bonuses_points',
            'berth_date',
            'city_id'
        ]


class IdImgSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['img_id_card']


class GetUserAPIView(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']


class GetProfileAPIView(serializers.ModelSerializer):
    url_edit = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        fields = [
            'id',
            'url_edit',
            'url',
            'user_id',
            'full_name',
            'first_name',
            'last_name',
            'img_id_card',
            'profile_img',
            'banned',
            'gender',
            'bonuses_points',
            'berth_date',
            'city_id',
            'account_type',
        ]

    def get_url_edit(self, obj):
        return f"/accounts/all-profile/{obj.pk}"

    def get_url(self, obj):
        return f"/accounts/all-profile/"


class ResetPassword(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = [
            'password',
            'confirm_password',
        ]

    def update(self, instance, validated_data):
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        if password != confirm_password:
            raise serializers.ValidationError({'password': 'password must match'})
        instance.set_password(password)
        instance.save()


class PreferredHerafiesAPI(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = PreferredHerafies
        fields = '__all__'

    def get_url(self, obj):
        return f"/accounts/herafi/preferred-herafi/{obj.pk}"
