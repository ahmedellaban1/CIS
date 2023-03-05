from django.urls import path
from .views import (
    add_tickets_api_view,
    tickets_api_details_view,
    get_all_tickets,
    ticket_status_api_view,
    herafi_all_ticket_api_view,

)

urlpatterns = [
    path('', add_tickets_api_view, name='add_tickets_api_view'),
    path('get_all_tickets/', get_all_tickets, name='get_all_tickets'),
    path('get_all_tickets/<int:pk>/', tickets_api_details_view, name='tickets_api_details_view'),
    path('herafi_all/', herafi_all_ticket_api_view, name='herafi_all_ticket_api_view'),
    path('herafi_all/<int:pk>', ticket_status_api_view, name='ticket_status_api_view'),

]
