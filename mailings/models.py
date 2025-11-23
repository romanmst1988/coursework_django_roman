from django.conf import settings
from django.db import models


class Recipient(models.Model):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    comment = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("view_all_recipients", "Can view all recipients"),
        ]

    def __str__(self):
        return self.email


class Message(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("view_all_messages", "Can view all messages"),
        ]

    def __str__(self):
        return self.subject


class Mailing(models.Model):
    STATUS_CHOICES = [
        ("Created", "Created"),
        ("Running", "Running"),
        ("Finished", "Finished"),
    ]
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    recipients = models.ManyToManyField(Recipient)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("view_all_mailings", "Can view all mailings"),
        ]

    def __str__(self):
        return f"Mailing {self.id} - {self.status}"


class MailingAttempt(models.Model):
    STATUS_CHOICES = [
        ("Success", "Success"),
        ("Failed", "Failed"),
    ]
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)
    attempt_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    server_response = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Attempt {self.id} - {self.status}"
