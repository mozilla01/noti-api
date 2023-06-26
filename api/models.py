from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Note(models.Model):
    user = models.ForeignKey(
        User, related_name="note", on_delete=models.CASCADE, null=True
    )
    title = models.CharField(max_length=100, default="Untitled")
    content = models.TextField(max_length=10000, default="", blank=True)

    def __str__(self):
        return self.title
