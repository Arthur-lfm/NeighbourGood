from django.contrib import admin
from .models import Poll, Choice, Vote


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ["description", "owner", "pub_date", "active"]
    search_fields = ["description", "owner__username"]
    list_filter = ["active"]
    date_hierarchy = "pub_date"


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ["choice_description", "poll"]
    search_fields = ["choice_description", "poll__description"]
    autocomplete_fields = ["poll"]


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ["choice", "poll", "user"]
    search_fields = ["choice__choice_description", "poll__description", "user__username"]
    autocomplete_fields = ["choice", "poll", "user"]
