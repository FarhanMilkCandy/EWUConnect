from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login, name='login'),
    path("logout/", views.logout,name="logout"),
    path("profile/", views.profile, name="profile")
    ]