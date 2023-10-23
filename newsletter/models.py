from django.db import models

from django.contrib.auth.models import User


class Newsletter(models.Model):
    email = models.EmailField(max_length=254, null=False, blank=False)
    subscribed_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-subscribed_on']

    def __str__(self):
        return self.email
