from django.contrib import admin
from business_manager.models import BusinessManager
from business_manager.models import BusinessManagerUserJoinTable

from business_manager.models import BusinessManagerAdmin
from business_manager.models import BusinessManagerUserJoinTableAdmin

# Register your models here.
admin.site.register(BusinessManager, BusinessManagerAdmin)
admin.site.register(BusinessManagerUserJoinTable, BusinessManagerUserJoinTableAdmin)
