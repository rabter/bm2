from django.db import models
from django.utils import timezone
from django.contrib import admin
from user.models import User


class BusinessManager(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=150)
    updated_by = models.CharField(max_length=150)

    name = models.CharField(max_length=150)
    primary_page = models.CharField(max_length=100)
    account_limit_count = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "business_managers"

class BusinessManagerAdmin(admin.ModelAdmin):
    list_display = ('name', 'primary_page', 'account_limit_count')

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


class BusinessManagerUserJoinTableAdmin(admin.ModelAdmin):
    list_display = ('getBusinessManagerId', 'getBusiness', 'getUserId', 'getUser', 'business_manager_role')

    def getBusinessManagerId(self, obj):
        return obj.business_manager.id

    def getUserId(self, obj):
        return obj.user.id

    def getBusiness(self, obj):
        return obj.business_manager.name

    def getUser(self, obj):
        return obj.user.firstname + ' ' + obj.user.lastname
