from django.shortcuts import render
from django.http import HttpResponse
from ad_account.models import AdAccount
from ad_account.serializers import AdAccountSerializer
from rest_framework.views import APIView
import json

class AdAccountList(APIView):

    def get(self, request, format=None):
        response_data = {}
        ad_account_list = AdAccount.objects.all()
        serializer = AdAccountSerializer(ad_account_list, many=True)

        response_data['data'] = serializer.data
        return HttpResponse(json.dumps(response_data), content_type="application/json")
