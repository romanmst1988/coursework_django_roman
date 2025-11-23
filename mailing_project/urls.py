from django.contrib import admin
from django.urls import include, path

from mailer.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    # Главная страница
    path("", index, name="index"),
    # Пользователи
    path("users/", include("users.urls", namespace="users")),
    # Mailings
    path("mailings/", include("mailings.urls", namespace="mailings")),
    # Старое приложение mailer
    path("messages/", include("mailer.urls", namespace="mailer")),
]
