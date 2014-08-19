from django.shortcuts import render_to_response
from django.template import RequestContext

from adverts.models import Advert


def home(request):

    adverts = (Advert.objects
                .filter(is_published=True)
                .order_by("-date_created"))

    return render_to_response("index.html", {
        "adverts": adverts
    }, RequestContext(request))
