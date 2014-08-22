from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from adverts.forms import AdvertCreationForm, PhotoCreationForm

from adverts.models import Advert
from messages.forms import NewMessageForm


def home(request):

    adverts = (Advert.objects
                .filter(is_published=True, end_date__gte=datetime.now())
                .order_by("-date_created"))

    return render_to_response("index.html", {
        "adverts": adverts
    }, RequestContext(request))


@login_required
def new_advert(request):
    form = AdvertCreationForm()
    success = False

    if request.method == "POST":
        form = AdvertCreationForm(request.POST)

        if form.is_valid():
            form.instance.user = request.user
            form.save()
            success = True

    return render_to_response("new_advert.html", {
        "form": form,
        "success": success,
    }, RequestContext(request))


def detail_advert(request, pk):
    advert = get_object_or_404(Advert, id=pk)

    message_sent = request.GET.get("message_sent")
    form = NewMessageForm()
    return render_to_response("detail.html", {
        "advert": advert,
        "form": form,
        "message_sent": message_sent
    }, RequestContext(request))


def photo_add(request, pk):
    advert = get_object_or_404(Advert, id=pk)
    form = PhotoCreationForm()

    if request.method == "POST":
        form = PhotoCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.advert = advert
            form.save()

            return redirect(reverse('detail_advert', args=[pk]))

    return render_to_response("photo_add.html", {
        "advert": advert,
        "form": form,
    }, RequestContext(request))
