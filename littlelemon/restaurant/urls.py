from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('api/menu/',views.MenuItemView.as_view()),
    path('api/menu/<int:pk>',views.SingleMenuItemView.as_view()),
    path('',views.home),
    path('api-token-auth/',obtain_auth_token)
   
]