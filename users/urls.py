# users/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView
from .views import register_view, logout_view, profile_view, profile_edit_view

app_name = 'users'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', profile_edit_view, name='profile_edit'),
]
