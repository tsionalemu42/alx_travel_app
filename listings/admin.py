from django.contrib import admin
from .models import Listing

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'location', 'available_from', 'available_to']
    list_filter = ['location', 'available_from']
    search_fields = ['title', 'description', 'location']
