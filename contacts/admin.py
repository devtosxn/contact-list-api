from django.contrib import admin
from .models import Contacts


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'address')
    list_filter = ('name', 'phone', 'email', 'address')
    search_fields = ('name', 'phone', 'email', 'address')
    list_per_page = 25


    
