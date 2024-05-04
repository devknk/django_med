from django.urls import path
from django.contrib import admin
from . import views
from account.views import (
    register_view,
    login_view,
    logout_view,
)

urlpatterns = [
    path('account/login/', login_view, name="login"),
    path('account/logout/', logout_view, name="logout"),
    path('account/register/', register_view, name="register"),
    ]