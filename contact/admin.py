from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'email', 'phone', 'message', 'date_sent')
    list_filter = ('author', 'email', 'date_sent')
    search_fields = ('author__username', 'name', 'date_sent')


admin.site.register(Contact, ContactAdmin)
