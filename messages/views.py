from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from adverts.models import Advert
from messages.forms import NewMessageForm
from messages.models import Conversation, Message


def new_message(request, pk):

    advert = get_object_or_404(Advert, id=pk)

    form = NewMessageForm(request.POST)

    if form.is_valid():
        text = form.cleaned_data.get("text")

        conversation = Conversation.objects.create(advert_id=pk)
        conversation.users.add(advert.user)
        conversation.users.add(request.user)

        message = conversation.messages.create(
            text=text,
            sender=request.user,
        )

        message.seen_users.add(request.user)

        redirect_to = "%(path)s?message_sent=true" % {
            "path": reverse("detail_advert", args=[pk])
        }

        return redirect(redirect_to)

    return HttpResponse("gonderilmedi")
