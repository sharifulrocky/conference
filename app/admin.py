from django.contrib import admin
from .models import *


def make_submitted(self, request, queryset):
    row_update = queryset.update(status='1')
    if row_update == 1:
        message_bit = '1 row'
    else:
        message_bit = '%s row(s)' % row_update
    self.message_user(request, '%s Submitted' % message_bit)

make_submitted.short_description = 'Marked as Submitted'


def make_cancelled(self, request, queryset):
    row_update = queryset.update(status='2')
    if row_update == 1:
        message_bit = '1 row'
    else:
        message_bit = '%s row(s)' % row_update
    self.message_user(request, '%s Cancelled' % message_bit)

make_cancelled.short_description = 'Marked as Cancelled'


class SessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'abstract', 'track', 'speaker', 'status')
    search_fields = ['title', 'abstract']  # Don't put foreign key field here
    list_filter = ('title', 'abstract', 'status')   # Don't put foreign key field here also

    actions = [make_submitted, make_cancelled]

admin.site.register(Session, SessionAdmin)


class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'bio')  # list_display is for showing list column name
    search_fields = ['name', 'title', 'bio']
    list_filter = ('name', 'title', 'bio')
    fieldsets = (
        ("General Information", {
            "fields": ("name", "title", "bio")
        }),
        ("Social Media", {
            'classes': ('collapse',),
            "fields": ("twitter", "facebook"),
            "description": "Add Social Media Here"
        })
    )

admin.site.register(Speaker, SpeakerAdmin)


class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ['title', 'description']
    list_filter = ('title', 'description')

admin.site.register(Track, TrackAdmin)
