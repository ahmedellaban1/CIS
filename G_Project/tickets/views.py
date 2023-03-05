from .serializer import (
    AddTicketAPI,
    Ticket,
    TicketAPIDetails,
    ALLTickets,
    TicketStatusAPI,

)
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import generics, status
# from rest_framework.decorators import api_view
from accounts.models import Profile, HerafiInformation  # type:ignore
from django.shortcuts import get_object_or_404
from .events import(
    views_requests_event,
    decrement_requests,
    rating, check_herafi_ticket_expiry,
    check_client_ticket_expiry,
)


# Create your views here.
class AddTicketsAPIView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = AddTicketAPI
    # lookup_field = 'pk'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        herafi = request.data['herafi']
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['client_id'] = request.user
        self.perform_create(serializer)
        views_requests_event(herafi_id=herafi)
        instance = serializer.data  # instance = self.get_object()
        return Response(instance, status=status.HTTP_201_CREATED)


add_tickets_api_view = AddTicketsAPIView.as_view()


class TicketsAPIDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketAPIDetails
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        partial = kwargs
        instance = self.get_object()
        user = request.user
        if user != instance.client_id:
            response = {
                "status": "task failed",
                "message": "forbidden you have not any permission to edit this info "
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        elif user == instance.client_id:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            rating(instance.herafi.id, float(request.data['evaluation']))
            response = {
                "status": "ticket updated successfully ",
                "all_data": serializer.data,
                "updated_data": request.data
            }
            return Response(response, status=status.HTTP_202_ACCEPTED)
        else:
            response = {
                "status": "task failed",
                "message": "something went error or user has no permission to edit this information "
            }
            return Response(response, status=status.HTTP_403_FORBIDDEN)

    def perform_update(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        partial = kwargs
        instance = self.get_object()
        user = request.user
        if user != instance.client_id:
            response = {
                "status": "task failed",
                "message": "forbidden you have not any permission to edit this info "
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        elif user == instance.client_id:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            decrement_requests(herafi_id=int(instance.herafi.id))
            self.perform_destroy(instance)
            response = {
                "status": "ticket deleted successfully ",
            }
            return Response(response, status=status.HTTP_202_ACCEPTED)
        else:
            response = {
                "status": "task failed",
                "message": "something went error or user has no permission to edit this information "
            }
            return Response(response, status=status.HTTP_403_FORBIDDEN)


tickets_api_details_view = TicketsAPIDetailsView.as_view()


class GetAllTickets(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = ALLTickets

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(client_id=request.user)
        check_client_ticket_expiry(client_id=request.user.id)
        serializer = ALLTickets(queryset, many=True)
        return Response(serializer.data)


get_all_tickets = GetAllTickets.as_view()


class TicketStatusAPIView(generics.RetrieveUpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketStatusAPI
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        user = request.user
        profile = get_object_or_404(Profile, user_id=user)
        try:
            herafi = get_object_or_404(HerafiInformation, profile_id=profile)
        except:
            response = {
                "status": "task failed",
                "message": "something went error or user has no permission to edit this information "
            }
            return Response(response, status=status.HTTP_403_FORBIDDEN)

        queryset = self.get_queryset().get(id=kwargs['pk'])
        serializer = ALLTickets(queryset, many=False)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs
        instance = self.get_object()
        user = request.user
        profile = get_object_or_404(Profile, user_id=user)
        try:
            herafi = get_object_or_404(HerafiInformation, profile_id=profile)
        except:
            response = {
                "status": "task failed",
                "message": "something went error or user has no permission to edit this information "
            }
            return Response(response, status=status.HTTP_403_FORBIDDEN)

        if herafi == instance.herafi:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            if request.data['status'] == 'been refused':
                decrement_requests(herafi_id=int(herafi.id))
            response = {
                "status": "ticket updated successfully ",
                "all_data": serializer.data,
                "updated_data": request.data
            }
            return Response(response, status=status.HTTP_202_ACCEPTED)
        else:
            response = {
                "status": "task failed",
                "message": "something went error or user has no permission to edit this information "
            }
            return Response(response, status=status.HTTP_403_FORBIDDEN)

    def perform_update(self, serializer):
        serializer.save()


ticket_status_api_view = TicketStatusAPIView.as_view()


class HerafiAllTicketAPIView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketStatusAPI
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        user = request.user
        profile = get_object_or_404(Profile, user_id=user)
        herafi = get_object_or_404(HerafiInformation, profile_id=profile)
        check_herafi_ticket_expiry(herafi_id=herafi.id)
        queryset = self.get_queryset().filter(herafi_id=herafi)
        serializer = ALLTickets(queryset, many=True)
        return Response(serializer.data)


herafi_all_ticket_api_view = HerafiAllTicketAPIView.as_view()
