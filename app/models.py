from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse


class Speaker(models.Model):
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=50)
    bio = models.TextField(max_length=1000)
    twitter = models.CharField(max_length=50, blank=True)
    facebook = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('speakers_detail', kwargs={'pk': self.pk})


class Track(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

SESSION_STATUS = (
    ('0', 'Draft'),
    ('1', 'Submitted'),
    ('2', 'Canceled')
)


class Session(models.Model):
    title = models.CharField(max_length=50)
    abstract = models.TextField(max_length=2000)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=SESSION_STATUS)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('sessions_detail', kwargs={'pk': self.pk})
