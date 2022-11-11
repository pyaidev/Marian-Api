from django.contrib import admin
from .models import *


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email')
    list_filter = ('id', 'name', 'phone',)
    search_fields = ['name', 'email', 'message']
    list_display_links = ('id', 'name', 'email')
    search_help_text = 'search on here'


admin.site.register(Contact, ContactAdmin)
