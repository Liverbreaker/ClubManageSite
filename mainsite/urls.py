from django.contrib import admin
from django.urls import path, include
from .views import (LoginView, LogoutView, IndexView, LogoutRedirectView, TestAuthView)

# "/"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('logout/redirect/', LogoutRedirectView.as_view(), name="logout_redir"),
    path('testauth/', TestAuthView.as_view(), name="check_auth")
]
