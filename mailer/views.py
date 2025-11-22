from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Count
from django.utils import timezone

# для кеширования
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from .models import Recipient, Message, Mailing, SendAttempt
from .forms import RecipientForm, MessageForm, MailingForm

@method_decorator(cache_page(60), name='dispatch')  # кеш на 60 секунд
class IndexView(generic.TemplateView):
    template_name = 'mailer/index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['total_mailings'] = Mailing.objects.count()
        ctx['active_mailings'] = Mailing.objects.filter(status=Mailing.STATUS_RUNNING).count()
        ctx['unique_recipients'] = Recipient.objects.count()
        return ctx

# Recipients
class RecipientListView(generic.ListView):
    model = Recipient

class RecipientCreateView(generic.CreateView):
    model = Recipient
    form_class = RecipientForm
    success_url = reverse_lazy('mailer:recipient_list')

class RecipientUpdateView(generic.UpdateView):
    model = Recipient
    form_class = RecipientForm
    success_url = reverse_lazy('mailer:recipient_list')

class RecipientDeleteView(generic.DeleteView):
    model = Recipient
    success_url = reverse_lazy('mailer:recipient_list')

# Messages
class MessageListView(generic.ListView):
    model = Message

class MessageCreateView(generic.CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailer:message_list')

class MessageUpdateView(generic.UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailer:message_list')

class MessageDeleteView(generic.DeleteView):
    model = Message
    success_url = reverse_lazy('mailer:message_list')

# Mailings
class MailingListView(generic.ListView):
    model = Mailing

class MailingCreateView(generic.CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailer:mailing_list')

class MailingUpdateView(generic.UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailer:mailing_list')

class MailingDeleteView(generic.DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailer:mailing_list')

class MailingDetailView(generic.DetailView):
    model = Mailing
