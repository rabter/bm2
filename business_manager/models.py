from django.db import models
from django.utils import timezone

class BusinessManager(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=150)
    updated_by = models.CharField(max_length=150)

    name = models.CharField(max_length=150)
    primary_page = models.CharField(max_length=100)
    account_limit_count = models.IntegerField()

    class Meta:
        db_table = "business_managers"
