from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list_create_api_view,name='product-list'), # list create view
    path('<int:pk>/', views.product_detail_api_view,name='product-detial'), # detail 
    path('<int:pk>/update/', views.product_update_api_view,name='product-put'),
    path('<int:pk>/delete/', views.product_distroy_api_view,name='product-delete'),
    # path('', views.product_alt_view,),
    # path('<int:pk>/', views.product_alt_view,),
    
]
