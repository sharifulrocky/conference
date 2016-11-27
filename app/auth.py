from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User


def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method == "GET":
        return render(request, "auth/login.html")

    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth.login(request, user)
                next = ""
                if "next" in request.GET:
                    next = request.GET["next"]
                if next is None or next == "":
                    next = "/"
                return redirect(next)
            else:
                return render(redirect, "auth/login.html", {"warning": "Your account is disabled"})
        else:
            return render(request, "auth/login.html", {"warning": "Invalid username and or password"})


def register(request):
    if request.method == "GET":
        return render(request, "auth/register.html")

    elif request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create_user(username, email, password).save()
        user = auth.authenticate(username=username, password=password)

        auth.login(request, user)
        return render(request, "auth/registered.html")
