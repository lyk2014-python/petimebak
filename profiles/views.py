from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import login as auth_login, logout as auth_logout

from profiles.forms import LoginForm


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username,
                                password=password)

            auth_login(request, user)

            return redirect(reverse("home"))


    return render_to_response("login.html", {
        "form": form
    }, RequestContext(request))


def logout(request):
    auth_logout(request)
    return render_to_response("logout.html", {},
                              RequestContext(request))
