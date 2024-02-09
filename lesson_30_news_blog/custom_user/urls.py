from django.contrib import admin
from django.urls import path, include

from custom_user.views import SignUpView, SignInView, ProfileView, LogoutView


urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
