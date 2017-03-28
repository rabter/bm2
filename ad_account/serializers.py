from ad_account.models import AdAccount
from rest_framework import serializers


class AdAccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = AdAccount
		fields = ('name', 'currency', 'timezone')
