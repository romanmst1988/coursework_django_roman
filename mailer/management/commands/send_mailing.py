import traceback

from django.core.mail import send_mail
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from mailer.models import Mailing, SendAttempt


class Command(BaseCommand):
    help = "Send mailing by id: python manage.py send_mailing <mailing_id>"

    def add_arguments(self, parser):
        parser.add_argument("mailing_id", type=int)

    def handle(self, *args, **options):
        mailing_id = options["mailing_id"]
        try:
            mailing = Mailing.objects.get(pk=mailing_id)
        except Mailing.DoesNotExist:
            raise CommandError("Mailing not found")

        self.stdout.write(f"Start sending for mailing {mailing_id}")

        mailing.status = Mailing.STATUS_RUNNING
        mailing.save(update_fields=["status"])

        recipients = mailing.recipients.all()
        for r in recipients:
            try:
                send_mail(
                    subject=mailing.message.subject,
                    message=mailing.message.body,
                    from_email=None,  # использует DEFAULT_FROM_EMAIL
                    recipient_list=[r.email],
                    fail_silently=False,
                )
                SendAttempt.objects.create(
                    mailing=mailing,
                    recipient=r,
                    status=SendAttempt.STATUS_OK,
                    server_response="OK (console backend)",
                )
                self.stdout.write(self.style.SUCCESS(f"Sent to {r.email}"))
            except Exception as e:
                SendAttempt.objects.create(
                    mailing=mailing,
                    recipient=r,
                    status=SendAttempt.STATUS_FAILED,
                    server_response=str(e) + "\n" + traceback.format_exc(),
                )
                self.stdout.write(self.style.ERROR(f"Failed to send to {r.email}: {e}"))
        if mailing.end_at <= timezone.now():
            mailing.status = Mailing.STATUS_FINISHED
            mailing.save(update_fields=["status"])
        self.stdout.write("Finished")
