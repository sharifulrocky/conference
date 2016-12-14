from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from app.models import *
from django.core.urlresolvers import reverse_lazy


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


class SessionCreate(CreateView):
    model = Session
    fields = ['title', 'abstract', 'track', 'speaker']


class SessionUpdate(UpdateView):
    model = Session
    fields = ['title', 'abstract', 'track', 'speaker']


class SessionDelete(DeleteView):
    model = Session
    success_url = reverse_lazy('sessions_list')


class SpeakerList(ListView):
    model = Speaker


class SpeakerDetails(DetailView):
    model = Speaker


class SpeakerCreate(CreateView):
    model = Speaker
    fields = ['name', 'title', 'bio']


class SpeakerUpdate(UpdateView):
    model = Speaker
    fields = ['name', 'title', 'bio']


class SpeakerDelete(DeleteView):
    model = Speaker
    success_url = reverse_lazy('speakers_list')
