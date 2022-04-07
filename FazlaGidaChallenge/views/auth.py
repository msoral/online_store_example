from django.contrib.auth import login as _login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from ..forms import SignUpForm


def signup(request) -> HttpResponse:
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            _login(request, user)
            return redirect("/")
    else:
        form = SignUpForm()
    return render(request, "auth/signup.html", {"form": form})


def login(request) -> HttpResponse:
    return render(request, "auth/login.html")
