from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('menu/',views.MenuItemView.as_view()),
    path('menu/<int:pk>',views.SingleMenuItemView.as_view()),
    path('home/',views.home),
    path('api-token-auth/',obtain_auth_token)
   
]