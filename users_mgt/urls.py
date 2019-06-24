from django.contrib import admin
from django.urls import path, include
from .views import SignupUserView, AccountView, SignupSuccessView

# "users/"

urlpatterns = [
    path('', AccountView.as_view(), name="admin"),
    path('signup/', SignupUserView.as_view(), name="signup"),
    path('signup/done/', SignupSuccessView.as_view(), name="signup_success"),

]
