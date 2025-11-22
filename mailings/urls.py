from django.urls import path
from . import views

app_name = 'mailings'

urlpatterns = [
    path('recipients/', views.recipient_list, name='recipient_list'),
    path('messages/', views.message_list, name='message_list'),
    path('mailings/', views.mailing_list, name='mailing_list'),
]
