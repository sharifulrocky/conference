from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


@login_required()
def secret(request):
    return render(request, 'restricted/secret.html')