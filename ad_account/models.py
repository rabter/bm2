from django.db import models
from django.utils import timezone

class AdAccount(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=150)
    updated_by = models.CharField(max_length=150)

    name = models.CharField(max_length=150)
    currency = models.CharField(max_length=50)
    timezone = models.CharField(max_length=100)

    class Meta:
        db_table = "ad_accounts"
