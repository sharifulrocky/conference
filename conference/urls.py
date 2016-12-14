"""conference URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app import auth, views


urlpatterns = [
    # Base url
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^login/', auth.login, name='login'),
    url(r'^logout/', auth.logout, name='logout'),
    url(r'^register/', auth.register, name='register'),
    url(r'^about/', views.about, name='about'),

    # Session url
    url(r'^sessions/$', views.SessionList.as_view(), name='sessions_list'),
    url(r'^sessions/(?P<pk>[0-9]+)/$', views.SessionDetail.as_view(), name='sessions_detail'),
    url(r'^sessions/create/$', views.SessionCreate.as_view(), name='sessions_create'),
    url(r'^sessions/update/(?P<pk>[0-9]+)/$', views.SessionUpdate.as_view(), name='sessions_update'),
    url(r'^sessions/delete/(?P<pk>[0-9]+)/$', views.SessionDelete.as_view(), name='sessions_delete'),

    # Speaker url
    url(r'^speaker/$', views.SpeakerList.as_view(), name='speakers_list'),
    url(r'^speaker/(?P<pk>[0-9]+)/$', views.SpeakerDetails.as_view(), name='speakers_detail'),
    url(r'^speaker/create/$', views.SpeakerCreate.as_view(), name='speakers_create'),
    url(r'^speaker/update/(?P<pk>[0-9]+)/$', views.SpeakerUpdate.as_view(), name='speakers_update'),
    url(r'^speaker/delete/(?P<pk>[0-9]+)/$', views.SpeakerDelete.as_view(), name='speakers_delete'),

    # User Session url
    url(r'^secret/', views.secret, name='secret'),
]

