from django.db import models
from datetime import datetime
from django.conf import settings
# Create your models here.


class Momento(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_at = models.DateTimeField(default=datetime.now, blank=True)
    lat = models.DecimalField(max_digits=18, decimal_places=14, blank=True)
    lng = models.DecimalField(max_digits=18, decimal_places=14, blank=True)
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
