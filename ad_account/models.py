from django.db import models
from django.utils import timezone
from business_manager.models import BusinessManager
from user.models import User
from django.contrib import admin

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

class AdAccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'currency', 'timezone')

class AdAccountBusinessManagerJoinTable(models.Model):
    USER_ACCOUNT_ROLE_ADMIN = 3
    USER_ACCOUNT_ROLE_ADVERTISER = 2
    USER_ACCOUNT_ROLE_ANALYST = 1

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    ad_account = models.ForeignKey('ad_account.AdAccount', db_constraint=False, null=False)
    business_manager = models.ForeignKey('business_manager.BusinessManager', db_constraint=False, null=False)

    owned_by = models.BooleanField(default=False)
    roles_given = models.IntegerField(default=USER_ACCOUNT_ROLE_ANALYST)

    class Meta:
        db_table = "ad_accounts_business_managers"
        unique_together = (("ad_account", "business_manager"),)

class AdAccountBusinessManagerJoinTableAdmin(admin.ModelAdmin):
    list_display = ('ad_account', 'business_manager', 'owned_by', 'roles_given')

class AdAccountUserJoinTable(models.Model):
    USER_ACCOUNT_ROLE_ADMIN = 3
    USER_ACCOUNT_ROLE_ADVERTISER = 2
    USER_ACCOUNT_ROLE_ANALYST = 1

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    ad_account = models.ForeignKey('ad_account.AdAccount', db_constraint=False, null=False)
    user = models.ForeignKey('user.User', db_constraint=False, null=False)

    current_role = models.IntegerField(default=USER_ACCOUNT_ROLE_ANALYST)

    class Meta:
        db_table = "ad_accounts_users"
        unique_together = (("ad_account", "user"),)

class AdAccountUserJoinTableAdmin(admin.ModelAdmin):
    list_display = ('ad_account', 'user', 'current_role', 'user_firstname')

    def user_firstname(self, obj):
        return obj.user.firstname
