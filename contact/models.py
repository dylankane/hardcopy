from django.db import models

from django.contrib.auth.models import User


class Contact(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_message')
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(
        max_length=20, null=True, blank=True)
    subject = models.CharField(max_length=250, null=True, blank=True)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_sent']

    def __str__(self):
        return f"{subject} by {name}"
