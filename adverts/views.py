from django.shortcuts import render_to_response
from django.template import RequestContext
from adverts.forms import AdvertCreationForm

from adverts.models import Advert


def home(request):

    adverts = (Advert.objects
                .filter(is_published=True)
                .order_by("-date_created"))

    return render_to_response("index.html", {
        "adverts": adverts
    }, RequestContext(request))

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
