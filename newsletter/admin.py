from django.contrib import admin
from .models import Newsletter


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_on',)
    list_filter = ('email', 'subscribed_on',)
    search_fields = ('email', 'subscribed_on',)


admin.site.register(Newsletter, NewsletterAdmin)
