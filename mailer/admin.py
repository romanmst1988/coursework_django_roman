from django.contrib import admin

from .models import Mailing, Message, Recipient, SendAttempt


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ("email", "full_name")


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("subject",)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ("id", "message", "status", "start_at", "end_at")
    list_filter = ("status", "start_at")
    filter_horizontal = ("recipients",)
    actions = ["send_now"]

    def send_now(self, request, queryset):
        from django.core import management  # type: ignore

        for mailing in queryset:
            management.call_command("send_mailing", str(mailing.id))
        self.message_user(request, "Запуск отправки для выбранных рассылок запущен.")

    send_now.short_description = "Отправить выбранные рассылки сейчас"  # type: ignore


@admin.register(SendAttempt)
class SendAttemptAdmin(admin.ModelAdmin):
    list_display = ("mailing", "recipient", "attempted_at", "status")
    list_filter = ("status",)
