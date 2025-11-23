from django.db import models
from django.utils import timezone


class Recipient(models.Model):
    email = models.EmailField(unique=True)
    full_name = models.CharField("Ф.И.О.", max_length=255, blank=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.email} ({self.full_name})"


class Message(models.Model):
    subject = models.CharField("Тема письма", max_length=255)
    body = models.TextField("Тело письма")

    def __str__(self):
        return self.subject


class Mailing(models.Model):
    STATUS_CREATED = "created"
    STATUS_RUNNING = "running"
    STATUS_FINISHED = "finished"
    STATUS_CHOICES = [
        (STATUS_CREATED, "Создана"),
        (STATUS_RUNNING, "Запущена"),
        (STATUS_FINISHED, "Завершена"),
    ]

    start_at = models.DateTimeField("Дата и время первой отправки")
    end_at = models.DateTimeField("Дата и время окончания отправки")
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=STATUS_CREATED
    )
    message = models.ForeignKey(
        Message, on_delete=models.PROTECT, related_name="mailings"
    )
    recipients = models.ManyToManyField(Recipient, related_name="mailings")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mailing {self.id} ({self.get_status_display()})"

    def is_active(self):
        now = timezone.now()
        return self.start_at <= now <= self.end_at


class SendAttempt(models.Model):
    STATUS_OK = "ok"
    STATUS_FAILED = "failed"
    STATUS_CHOICES = [
        (STATUS_OK, "Успешно"),
        (STATUS_FAILED, "Не успешно"),
    ]

    mailing = models.ForeignKey(
        Mailing, on_delete=models.CASCADE, related_name="attempts"
    )
    recipient = models.ForeignKey(
        Recipient, on_delete=models.CASCADE, related_name="attempts"
    )
    attempted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    server_response = models.TextField(blank=True)

    def __str__(self):
        return (
            f"{self.mailing_id} -> {self.recipient.email} [{self.get_status_display()}]"
        )
