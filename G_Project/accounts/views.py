from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics, status, mixins
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Profile, HerafiInformation
from django.shortcuts import get_object_or_404
from main_info.models import Job
from .serializer import (
    CreateUserAPI,
    AutoUpdateProfileSerializer,
    CreateHerafiIfoAPI,
    UpdateProfileAPI,
    IdImgSerializer,
    GetUserAPIView,
    GetProfileAPIView,
    ResetPassword,
)

# Create your views here.


def fullname(full_name):
    name = full_name.split()
    if len(name) != 0 < 2 or len(name) != 0:
        f_name = name[0]
        l_name = name[-1]
        return f_name, l_name
    return None


class CreateUserAPIView(generics.CreateAPIView):
    """
        all data in this endpoint are required
    """

    queryset = User.objects.all()
    serializer_class = CreateUserAPI
    lookup_field = 'pk'
    authentication_classes = []
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = User.objects.get(username=serializer.data['username'])
        token = Token.objects.create(user=user)
        profile = Profile.objects.get(user_id=user)

        first_name, last_name = fullname(serializer.data['full_name'])
        ser2 = AutoUpdateProfileSerializer(profile,
                                           data={
                                               'full_name': serializer.data['full_name'],
                                               'first_name': first_name,
                                               'last_name': last_name,
                                               'account_type': int(serializer.data['account_type']),
                                               'gender': bool(serializer.data['gender'])
                                           }
                                           )
        account_type = int(serializer.data['account_type'])
        if ser2.is_valid():
            ser2.save()
            if account_type == 2:
                job_category = int(serializer.data['job_category'])
                job = Job.objects.get(id=job_category)
                HerafiInformation.objects.create(profile_id=profile, job_category=job)

        response = {
            'status': 'user created successfully',
            'token': token.key,
            'user_id': user.id,
            'profile_id': profile.id,
            'username': user.username,
            'full_name': profile.full_name,
            'first_name': profile.first_name,
            'last_name': profile.last_name,
            'account_type': f"{profile.account_type}"

        }
        return Response(response, status=status.HTTP_201_CREATED)


create_user_api_view = CreateUserAPIView.as_view()


@api_view(['POST'])
@authentication_classes([])
@permission_classes([AllowAny])
def log_in(request):
    """
    this end point take two parameters (username, password)
    {
    "username":"ahmed",
    "password":"ahmed"
    }
    """
    method = request.method

    if method == "POST":
        if list(request.data.keys()) != ["username", "password"]:
            username = None
            password = None
        else:
            username = request.data['username']
            password = request.data['password']
        if username is None or password is None:
            response = {
                "status": "missed parameter",
                "username": "this field is require",
                "password": "this field is require"
            }
            return Response(response)

        user = authenticate(username=username, password=password)
        if user:
            token = Token.objects.get_or_create(user=user)
            profile = Profile.objects.get(user_id=user)
            response = {
                "message": " login successfully ",
                "token": f"{token[0]}",
                'id': user.id,
                'username': user.username,
                'full_name': profile.full_name,
                'first_name': profile.first_name,
                'last_name': profile.last_name,
                'account_type': f"{profile.account_type}"
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response({"status": "invalid data ", "message": "invalid username or password"}, status=400)


class UpdateProfileAPIView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = UpdateProfileAPI
    lookup_field = 'user_id'

    def update(self, request, *args, **kwargs):
        partial = kwargs
        instance = self.get_object()
        if request.user.id == kwargs['user_id']:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            response = {
                "status": "profile updated successfully",
                "full_name": f"{instance.full_name}",
                "first_name": f"{instance.first_name}",
                "last_name": f"{instance.last_name}",
                "profile_img": f"{instance.profile_img}",
                "bonuses_points": f"{instance.bonuses_points}",
                "berth_date": f"{instance.berth_date}",
                "city_id": f"{instance.city_id}",
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {
                "status": "user have no permission to edit this profile",
            }
            return Response(response, status=status.HTTP_403_FORBIDDEN)

    def perform_update(self, serializer):
        if serializer.is_valid(raise_exception=True):
            full_mame = serializer.validated_data['full_name']
            first_name = serializer.validated_data['first_name']
            last_name = serializer.validated_data['last_name']
            f_name, l_name = fullname(full_mame)
            if first_name is None and last_name is None:
                instance = serializer.save(first_name=f_name, last_name=l_name)
            elif first_name is None and last_name is not None:
                instance = serializer.save(first_name=f_name)
            elif first_name is not None and last_name is None:
                instance = serializer.save(last_name=l_name)
            else:
                instance = serializer.save()


update_profile = UpdateProfileAPIView.as_view()


@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def log_out(request, *args, **kwargs):
    """
    {
    this end point take 0 parameters
    }
    """
    method = request.method

    if method == "DELETE":
        if request.user.id == kwargs['pk']:
            user = User.objects.get(id=kwargs['pk'])
            token = Token.objects.get(user=user)
            token.delete()
            response = {
                "status": "200",
                "message": "logout successfully",
                "token": "token deleted from database",
            }
            return Response(response, status=status.HTTP_202_ACCEPTED)
        response = {
            "status": "403 Forbidden",
            "message": "user id != the user that logged in id",
        }
        return Response(response, status=status.HTTP_403_FORBIDDEN)


class NationalIdImage(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = IdImgSerializer
    lookup_field = 'user_id'

    def update(self, request, *args, **kwargs):
        partial = kwargs
        instance = self.get_object()
        if 'img_id_card' not in request.data:
            response = {
                "status": "task failed",
                "message": "this end point take img_id_card, and img_id_card is required field can't be null value "
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        elif request.user.id == kwargs['user_id']:
            if request.data['img_id_card'] != '':
                serializer = self.get_serializer(instance, data=request.data, partial=partial)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)
                response = {
                    "status": "image uploaded successfully",
                    "img": f"{serializer.data['img_id_card']}"
                }
                return Response(response, status=status.HTTP_202_ACCEPTED)
            response = {
                "status": "task failed",
                "message": "img_id_card is required field can't be null value "
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            response = {
                "status": "task failed",
                "message": "something went error or user has no permission to edit this information "
            }
            return Response(response, status=status.HTTP_403_FORBIDDEN)

    def perform_update(self, serializer):
        serializer.save()
        if not serializer.data['img_id_card']:
            serializer.data['img_id_card'] = None


national_id_image = NationalIdImage.as_view()


class AllProfileAPIView(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        generics.GenericAPIView):
    queryset = Profile.objects.all()
    serializer_class = GetProfileAPIView
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        elif pk is None:
            return self.list(request, *args, **kwargs)


get_all_profile = AllProfileAPIView().as_view()


class AllUserAPIView(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     generics.GenericAPIView):
    queryset = User.objects.all()
    lookup_field = 'pk'
    serializer_class = GetUserAPIView

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        elif pk is None:
            return self.list(request, *args, **kwargs)


all_user = AllUserAPIView.as_view()


@api_view(['PUT'])
def reset_password_api_view(request, pk, *args, **kwargs):

    """
        {
        "id":1,
        "username":"ahmed",
        "old_password":"ahmed",
        "password":"ellaban",
        "confirm_password":"ellaban"
        }
        password : the new one
        old_password : current password
    """
    if request.user.id == pk:
        queryset = get_object_or_404(User, pk=pk)
        method = request.method
        if method == "PUT":
            if list(request.data.keys()) != ['id', 'username', 'old_password', 'password', 'confirm_password']:
                response = {
                    "status": "Error data not valid",
                    "message": "this endpoint should contain this fields "
                               "['id', 'username', 'old_password', 'password', 'confirm_password'] "
                }
                return Response(response)
            else:
                username = request.data['username']
                password = request.data['old_password']
            if username is None or password is None:
                response = {
                    "status": "missed parameter",
                    "username": "this field is require",
                    "password": "this field is require"
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            user = authenticate(username=username, password=password)
            if user:
                data = {'password': request.data['password'], 'confirm_password': request.data['confirm_password']}
                serializer = ResetPassword(queryset, many=False, data=data)
                if serializer.is_valid(raise_exception=True):
                    serializer.update(instance=queryset, validated_data=username)
                    return Response(serializer.data, status=200)
            elif not user:
                response = {
                    "status": "Error ",
                    "message": "invalid username or password",
                }
                return Response(response, status=status.HTTP_401_UNAUTHORIZED)

    elif request.user.id != pk:
        response = {
            "status": "FORBIDDEN",
            "message": "user have no permission to edit this data",
        }
        return Response(response, status=status.HTTP_403_FORBIDDEN)


"""
@api_view(['PUT'])
def update_profile(request, id):
    method = request.method
    print(f"{request.data} {id}")
    # and request.user.id == id
    if method == 'PUT':
        queryset = Profile.objects.get(user_id=id)
        serializer = UpdateProfileAPI(queryset, request.data)
        if serializer.is_valid(raise_exception=True):
            full_mame = serializer.validated_data['full_name']
            first_name = serializer.validated_data['first_name']
            last_name = serializer.validated_data['last_name']
            f_name, l_name = fullname(full_mame)
            if first_name is None and last_name is None:
                instance = serializer.save(first_name=f_name, last_name=l_name)
            elif first_name is None and last_name is not None:
                instance = serializer.save(first_name=f_name)
            elif first_name is not None and last_name is None:
                instance = serializer.save(last_name=l_name)
            else:
                instance = serializer.save()

            response = {
                "status": "profile updated successfully",
                "full_name": f"{instance.full_name}",
                "first_name": f"{instance.first_name}",
                "last_name": f"{instance.last_name}",
                "profile_img": f"{instance.profile_img}",
                "bonuses_points": f"{instance.bonuses_points}",
                "berth_date": f"{instance.berth_date}",
                "city_id": f"{instance.city_id}",
            }
            return Response(response, status=status.HTTP_200_OK)

        response = {
            "status": "Error data not valid or somthing went error ",
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    response = {
        "status": "user have no permission to edit this profile",
    }
    return Response(response, status=status.HTTP_404_NOT_FOUND)

"""