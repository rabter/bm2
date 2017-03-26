from django.db import models
from django.utils import timezone
from user.models import User

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

class BusinessManagerUserJoinTable(models.Model):
    ADMIN = 'admin'
    EMPLOYEE = 'employee'

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    business_manager = models.ForeignKey('business_manager.BusinessManager', db_constraint=False, null=False)
    user = models.ForeignKey('user.User', db_constraint=False, null=False)

    business_manager_role = models.CharField(max_length=30)

    class Meta:
        db_table = "business_managers_users"
        unique_together = (("business_manager", "user"),)
