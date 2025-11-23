from django.contrib import admin
from django.urls import path, include

from mailer import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mailer.urls', namespace='mailer')),
    path('', include('mailer.urls')),
    path('', include('mailings.urls')),
    path('', include('users.urls')),
    path('users/', include('users.urls')),
    path('', views.index, name='mailer.index')  # type: ignore
]
