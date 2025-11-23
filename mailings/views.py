from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import Mailing, MailingAttempt, Message, Recipient


@login_required
def recipient_list(request):
    recipients = Recipient.objects.filter(owner=request.user)
    return render(request, "mailings/recipient_list.html", {"recipients": recipients})


@login_required
def message_list(request):
    messages = Message.objects.filter(owner=request.user)
    return render(request, "mailings/message_list.html", {"messages": messages})


@login_required
def mailing_list(request):
    mailings = Mailing.objects.filter(owner=request.user)
    return render(request, "mailings/mailing_list.html", {"mailings": mailings})
