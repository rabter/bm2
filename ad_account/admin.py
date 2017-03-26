from django.contrib import admin
from ad_account.models import AdAccount
from ad_account.models import AdAccountBusinessManagerJoinTable
from ad_account.models import AdAccountUserJoinTable

# Register your models here.
admin.site.register(AdAccount)
admin.site.register(AdAccountBusinessManagerJoinTable)
admin.site.register(AdAccountUserJoinTable)
