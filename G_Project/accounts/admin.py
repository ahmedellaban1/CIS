from django.contrib import admin
from .models import Profile, AccountType, PreferredHerafies, HerafiInformation
# Register your models here.
admin.site.register(Profile)
admin.site.register(AccountType)
admin.site.register(PreferredHerafies)
admin.site.register(HerafiInformation)
