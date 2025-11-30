from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class SelfMessage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
