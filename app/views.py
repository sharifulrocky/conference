from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from app.models import *


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


@login_required()
def secret(request):
    return render(request, 'restricted/secret.html')


class SessionList(ListView):
    model = Session


class SessionDetail(DetailView):
    model = Session
