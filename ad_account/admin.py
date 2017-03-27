from django.contrib import admin
from ad_account.models import AdAccount
from ad_account.models import AdAccountBusinessManagerJoinTable
from ad_account.models import AdAccountUserJoinTable

from ad_account.models import AdAccountAdmin
from ad_account.models import AdAccountBusinessManagerJoinTableAdmin
from ad_account.models import AdAccountUserJoinTableAdmin

# Register your models here.
admin.site.register(AdAccount, AdAccountAdmin)
admin.site.register(AdAccountBusinessManagerJoinTable, AdAccountBusinessManagerJoinTableAdmin)
admin.site.register(AdAccountUserJoinTable, AdAccountUserJoinTableAdmin)
