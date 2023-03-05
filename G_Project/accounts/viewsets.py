from rest_framework import viewsets, mixins
from .serializer import HerafiIfoAPI, Profile, PreferredHerafiesAPI
from .models import HerafiInformation, PreferredHerafies
from rest_framework.response import Response
from rest_framework import status


class HerafiViewSetsAPIView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = HerafiInformation.objects.all()
    serializer_class = HerafiIfoAPI
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        profile = Profile.objects.get(user_id=request.user.id)

        try:
            herafi_info = HerafiInformation.objects.get(profile_id=profile)
        except:
            response = {
                "status": "not found",
                "message": "this user may be client user not a herafi "
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        if int(herafi_info.id) == int(kwargs['pk']):
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=int(kwargs['pk']))
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            response = {
                "status": "information updated successfully",
                "id": f"{herafi_info.id}",
                "views": f"{herafi_info.views}",
                "requests": f"{herafi_info.requests}",
                "price_of_preview": f"{herafi_info.price_of_preview}",
                "experiences": f"{herafi_info.experiences}",
                "phone_number": f"{herafi_info.phone_number}",
                "bio": f"{herafi_info.bio}",
                "job_category": f"{herafi_info.job_category}",
                "profile_id": f"{herafi_info.profile_id}",

            }
            return Response(response, status=status.HTTP_200_OK)

        response = {
            "status": "FORBIDDEN",
            "message": "user have no permission to edit this data",
        }
        return Response(response, status=status.HTTP_403_FORBIDDEN)


class PreferredHerafi(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = PreferredHerafies.objects.all()
    serializer_class = PreferredHerafiesAPI
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        profile = Profile.objects.get(user_id=request.user.id)

        try:
            preferred_herafi = PreferredHerafiesAPI.objects.get(client_profile_id=profile)
        except:
            response = {
                "status": "not found",
                "message": "this user may be client user not a herafi "
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        if int(preferred_herafi.id) == int(kwargs['pk']):
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=int(kwargs['pk']))
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            response = {
                "status": "information updated successfully",
                "id": f"{preferred_herafi.id}",
                "client_profile_id": f"{preferred_herafi.client_profile_id}",
                "herafi_id": f"{preferred_herafi.herafi_id}",

            }
            return Response(response, status=status.HTTP_200_OK)

        response = {
            "status": "FORBIDDEN",
            "message": "user have no permission to edit this data",
        }
        return Response(response, status=status.HTTP_403_FORBIDDEN)


