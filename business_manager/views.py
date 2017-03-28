from django.shortcuts import render
from django.http import HttpResponse
from business_manager.models import BusinessManager
from business_manager.models import BusinessManagerUserJoinTable
from user.models import User
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

class PeopleAndAssetList(APIView):

    def get(self, request, format=None):

        response_data = {}
        try:
            people_and_assets = []
            business_managers = BusinessManager.objects.all()
            for bm in business_managers:
                bm_dict = {}

                bm_dict['name'] = bm.name
                bm_dict['primary_page'] = bm.primary_page
                bm_dict['account_limit_count'] = bm.account_limit_count

                users_of_business = BusinessManagerUserJoinTable.objects.filter(business_manager_id = bm.id)
                users = []
                for user in users_of_business:
                    user_dict = {}
                    user = User.objects.get(pk=user.id)
                    user_dict['firstname'] = user.firstname
                    user_dict['lastname'] = user.lastname
                    user_dict['email'] = user.email
                    users.append(user_dict)
                bm_dict['people'] = users

                people_and_assets.append(bm_dict)
            response_data['success'] = 'YES'
            response_data['data'] = people_and_assets
            response_data['total_count'] = len(people_and_assets)
        except Exception as e:
            response_data['success'] = 'NO'
            response_data['msg'] = str(e)

        return HttpResponse(json.dumps(response_data), content_type="application/json")
