from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def index(request):
    return render(request, "login/index.html")

def register(request):
    response = User.objects.register(
        request.POST["first"],
        request.POST["last"],
        request.POST["email"],
        request.POST["password"],
        request.POST["confirm"],
        request.POST["dob"],
    )
    print response
    if response["valid"]:
        request.session["user_id"] = response["user"].id
        return redirect("/home")
    else:
        for error_messages in response["errors"]:
            messages.add_message(request, messages.ERROR, error_messages)
        return redirect("/")

def login(request):
    response = User.objects.login(
        request.POST["email"],
        request.POST["password"]
    )
    print response
    if response["valid"]:
        request.session["user_id"] = response["user"].id
        return redirect("/home")
    else:
        for error_messages in response["errors"]:
            messages.add_message(request, messages.ERROR, error_messages)
        return redirect("/")

    return redirect("/")

def logout(request):
    request.session.clear()
    messages.add_message(request, messages.SUCCESS, "You have just logged out, goodbye!")
    return redirect("/")
