# для кеширования
from django.shortcuts import render  # type: ignore
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic  # type: ignore
from django.views.decorators.cache import cache_page

from .forms import MailingForm, MessageForm, RecipientForm
from .models import Mailing, Message, Recipient, SendAttempt


def index(request):
    return render(request, "mailer/index.html")


class IndexView(generic.TemplateView):
    template_name = "mailer/index.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["total_mailings"] = Mailing.objects.count()
        ctx["active_mailings"] = Mailing.objects.filter(status="Запущена").count()
        ctx["unique_recipients"] = Recipient.objects.count()
        return ctx


class RecipientListView(generic.ListView):
    model = Recipient
    template_name = "mailer/recipient_list.html"


class RecipientCreateView(generic.CreateView):
    model = Recipient
    form_class = RecipientForm
    template_name = "mailer/recipient_form.html"
    success_url = reverse_lazy("mailer:recipient_list")


class RecipientUpdateView(generic.UpdateView):
    model = Recipient
    form_class = RecipientForm
    template_name = "mailer/recipient_form.html"
    success_url = reverse_lazy("mailer:recipient_list")


class RecipientDeleteView(generic.DeleteView):
    model = Recipient
    template_name = "mailer/recipient_confirm_delete.html"
    success_url = reverse_lazy("mailer:recipient_list")


class MessageListView(generic.ListView):
    model = Message
    template_name = "mailer/message_list.html"
    context_object_name = "object_list"  # по умолчанию уже object_list


class MessageCreateView(generic.CreateView):
    model = Message
    form_class = MessageForm
    template_name = "mailer/message_form.html"
    success_url = reverse_lazy("mailer:message_list")


class MessageDetailView(generic.DetailView):
    model = Message
    template_name = "mailer/message_detail.html"
    context_object_name = "object"


class MessageUpdateView(generic.UpdateView):
    model = Message
    form_class = MessageForm
    template_name = "mailer/message_form.html"
    success_url = reverse_lazy("mailer:message_list")


class MessageDeleteView(generic.DeleteView):
    model = Message
    template_name = "mailer/message_confirm_delete.html"
    success_url = reverse_lazy("mailer:message_list")


class MailingListView(generic.ListView):
    model = Mailing
    template_name = "mailer/mailing_list.html"


class MailingCreateView(generic.CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = "mailer/mailing_form.html"
    success_url = reverse_lazy("mailer:mailing_list")


class MailingDetailView(generic.DetailView):
    model = Mailing
    template_name = "mailer/mailing_detail.html"


class MailingUpdateView(generic.UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = "mailer/mailing_form.html"
    success_url = reverse_lazy("mailer:mailing_list")


class MailingDeleteView(generic.DeleteView):
    model = Mailing
    template_name = "mailer/mailing_confirm_delete.html"
    success_url = reverse_lazy("mailer:mailing_list")


@method_decorator(cache_page(60), name="dispatch")  # кеш на 60 секунд
class IndexView(generic.TemplateView):  # type: ignore
    template_name = "mailer/index.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["total_mailings"] = Mailing.objects.count()
        ctx["active_mailings"] = Mailing.objects.filter(
            status=Mailing.STATUS_RUNNING
        ).count()
        ctx["unique_recipients"] = Recipient.objects.count()
        return ctx


# Recipients
class RecipientListView(generic.ListView):  # type: ignore
    model = Recipient


class RecipientCreateView(generic.CreateView):  # type: ignore
    model = Recipient
    form_class = RecipientForm
    success_url = reverse_lazy("mailer:recipient_list")


class RecipientUpdateView(generic.UpdateView):  # type: ignore
    model = Recipient
    form_class = RecipientForm
    success_url = reverse_lazy("mailer:recipient_list")


class RecipientDeleteView(generic.DeleteView):  # type: ignore
    model = Recipient
    success_url = reverse_lazy("mailer:recipient_list")


# Messages
class MessageListView(generic.ListView):  # type: ignore
    model = Message


class MessageCreateView(generic.CreateView):  # type: ignore
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailer:message_list")


class MessageUpdateView(generic.UpdateView):  # type: ignore
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailer:message_list")


class MessageDeleteView(generic.DeleteView):  # type: ignore
    model = Message
    success_url = reverse_lazy("mailer:message_list")


# Mailings
class MailingListView(generic.ListView):  # type: ignore
    model = Mailing


class MailingCreateView(generic.CreateView):  # type: ignore
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("mailer:mailing_list")


class MailingUpdateView(generic.UpdateView):  # type: ignore
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("mailer:mailing_list")


class MailingDeleteView(generic.DeleteView):  # type: ignore
    model = Mailing
    success_url = reverse_lazy("mailer:mailing_list")


class MailingDetailView(generic.DetailView):  # type: ignore
    model = Mailing
