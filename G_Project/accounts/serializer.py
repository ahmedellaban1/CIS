from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .models import (
                    Profile,
                    AccountType,
                    PreferredHerafies,
                    HerafiInformation
)
from .models import profile_img_uploader


class CreateUserAPI(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    account_type = serializers.CharField(style={'input_type': 'text'})
    job_category = serializers.CharField(style={'input_type': int})
    gender = serializers.BooleanField(style={'input_type': bool})


    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
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


class CreateHerafiIfoAPI(serializers.ModelSerializer):
    class Meta:
        model = HerafiInformation
        fields = ['profile_id', 'job_category']


class UpdateProfileAPI(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False, allow_null=True,)
    last_name = serializers.CharField(required=False, allow_null=True,)
    profile_img = serializers.ImageField(required=False, allow_null=True)

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
    class Meta:
        model = Profile
        fields = [
            'id',
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

