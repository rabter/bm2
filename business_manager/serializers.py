from business_manager.models import BusinessManager
from rest_framework import serializers


class BusinessManagerSerializer(serializers.ModelSerializer):
	class Meta:
		model = BusinessManager
		fields = ('name', 'primary_page', 'account_limit_count')
