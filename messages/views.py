from django.core.urlresolvers import reverse
from django.db import models
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from adverts.models import Advert
from messages.forms import NewMessageForm
from messages.models import Conversation, Message


def new_message(request, pk):

    advert = get_object_or_404(Advert, id=pk)

    form = NewMessageForm(request.POST)

    if form.is_valid():
        text = form.cleaned_data.get("text")

        conversation = Conversation.objects.create(advert_id=pk)
        conversation.users.add(request.user)
        conversation.users.add(advert.user)

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


def inbox(request):

    conversations = Conversation.objects.filter(
        users=request.user,
    ).annotate(
        message_count=models.Count("messages")
    ).exclude(
        message_count=0
    ).order_by(
        "-date_created"
    )

    return render_to_response("inbox.html", {
        "conversations": conversations
    }, RequestContext(request))


def conversation_detail(request, pk):

    conversation = get_object_or_404(
        Conversation, users=request.user, id=pk)

    messages = conversation.messages.all()

    form = NewMessageForm()

    if request.method == "POST":
        form = NewMessageForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data.get("text")

            conversation.messages.create(
                sender=request.user,
                text=message)

            form = NewMessageForm()

    # mark as seen current messages
    unread_messages = Message.objects.filter(
        conversation=conversation
    ).exclude(
        seen_users=request.user
    )

    for message in unread_messages:
        message.seen_users.add(request.user)

    return render_to_response("conversation_detail.html", {
        "conversation": conversation,
        "messages": messages,
        "form": form
    }, RequestContext(request))
