from django.urls import path
from .views import (
    create_user_api_view,
    log_in,
    reset_password_api_view,
    update_profile,
    log_out,
    national_id_image,
    get_all_profile,
    all_user,
)

app_name = 'accounts'

urlpatterns = [
    path('', create_user_api_view, name='create-user-api-view'),
    path('login/', log_in, name='login-api-view'),
    path('update-profile/<int:user_id>', update_profile, name='update-profile-view'),
    path('logout/<int:pk>', log_out, name='logout'),
    path('id_image/<int:user_id>', national_id_image, name='id_image'),
    path('all-profile/', get_all_profile, name='get_all_profile'),
    path('all-profile/<int:pk>', get_all_profile, name='get-profile_details'),
    path('all-user', all_user, name='all_user'),
    path('all-user/<int:pk>', all_user, name='user_detail'),
    path('reset-password/<int:pk>', reset_password_api_view, name='reset_password_api_view'),
]
