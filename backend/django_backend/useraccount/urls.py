from django.urls import path 

from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogouView, UserDatailsView
from rest_framework_simplejwt import TokenVerifyView

urlpatterns = [
    path('register/', RegisterView.as_View(), name="rest_register"),
    path("login/", Login.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
]


