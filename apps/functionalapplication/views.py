from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import User, cite
from django.contrib import messages

def current_user(request):
	return User.objects.get(id = request.session['user_id'])

def home(request):
	user = current_user(request)

	data = {
		'user': user,
		'cite': cite.objects.exclude(favorites = user),
		'favorites': user.favorites.all()
	}

	return render(request, "functionalapplication/index.html", data)



def add_cite(request):

    response = cite.objects.add(
        request.POST["quoter"],
        request.POST["quote"],
    )
    print response
    if response["valid"]:
	cite.objects.create(
		quoter = request.POST["quoter"],
		quote = request.POST["quote"],
		uploader_id = request.session["user_id"]
	)
        return redirect("/home")
    else:
        for error_messages in response["errors"]:
            messages.add_message(request, messages.ERROR, error_messages)
        return redirect("/home")


def add_favorite(request, id):

	user = current_user(request)
	favorite = cite.objects.get(id=id)

	user.favorites.add(favorite)
	return redirect('/home')


def remove_favorite(request, id):

	user = current_user(request)
	favorite =  cite.objects.get(id=id)

	user.favorites.remove(favorite)
	return redirect('/home')


def show_user(request, id):

	user =  User.objects.get(id = id)
	userdata = {
		'user': user,
		'favorites': user.favorites.all()		
	}
	return render(request, "functionalapplication/user.html", userdata)
