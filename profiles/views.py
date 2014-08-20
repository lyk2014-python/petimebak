from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate

from profiles.forms import LoginForm, RegistrationForm


def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            auth_login(request, form.user)
            return redirect(reverse("home"))

    return render_to_response("login.html", {
        "form": form,
    }, RequestContext(request))


def logout(request):
    auth_logout(request)
    return render_to_response("logout.html", {},
                              RequestContext(request))

def register(request):
    form = RegistrationForm()

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username,
                                password=password)
            auth_login(request, user)
            return redirect(reverse("home"))

    return render_to_response("register.html", {
        "form": form
    }, RequestContext(request))
