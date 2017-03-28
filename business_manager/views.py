from django.shortcuts import render
from django.http import HttpResponse
from business_manager.models import BusinessManager
from business_manager.serializers import BusinessManagerSerializer
from rest_framework.views import APIView
import json

class BusinessManagerList(APIView):

    def get(self, request, format=None):
        response_data = {}
        business_manager_list = BusinessManager.objects.all()
        serializer = BusinessManagerSerializer(business_manager_list, many=True)

        response_data['data'] = serializer.data
        return HttpResponse(json.dumps(response_data), content_type="application/json")
