from django.contrib import admin
from business_manager.models import BusinessManager
from business_manager.models import BusinessManagerUserJoinTable

# Register your models here.
admin.site.register(BusinessManager)
admin.site.register(BusinessManagerUserJoinTable)
