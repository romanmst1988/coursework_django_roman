from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipient, Message, Mailing, MailingAttempt
from .forms import RecipientForm, MessageForm, MailingForm

@login_required
def recipient_list(request):
    recipients = Recipient.objects.filter(owner=request.user)
    return render(request, 'mailings/recipient_list.html', {'recipients': recipients})

@login_required
def message_list(request):
    messages = Message.objects.filter(owner=request.user)
    return render(request, 'mailings/message_list.html', {'messages': messages})

@login_required
def mailing_list(request):
    mailings = Mailing.objects.filter(owner=request.user)
    return render(request, 'mailings/mailing_list.html', {'mailings': mailings})
