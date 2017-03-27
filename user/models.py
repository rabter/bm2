from django.db import models
from django.contrib import admin
from django.utils import timezone

class User(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=150)
    updated_by = models.CharField(max_length=150)

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    class Meta:
        db_table = "users"

class UserAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email')
