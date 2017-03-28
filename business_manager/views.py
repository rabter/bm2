from django.shortcuts import render
from django.http import HttpResponse
from business_manager.models import BusinessManager
from business_manager.models import BusinessManagerUserJoinTable
from ad_account.models import AdAccountBusinessManagerJoinTable
from user.models import User
from ad_account.models import AdAccount
from ad_account.models import AdAccountUserJoinTable
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
                for business_user in users_of_business:
                    user_dict = {}
                    user = User.objects.get(pk=business_user.user_id)
                    user_dict['firstname'] = user.firstname
                    user_dict['lastname'] = user.lastname
                    user_dict['email'] = user.email
                    user_dict['business_manager_role'] = business_user.business_manager_role
                    users.append(user_dict)
                bm_dict['people'] = users

                ad_accounts_of_business = AdAccountBusinessManagerJoinTable.objects.filter(business_manager_id = bm.id)
                ad_accounts = []
                for business_account in ad_accounts_of_business:
                    ad_account_dict = {}
                    ad_account = AdAccount.objects.get(pk=business_account.ad_account_id)
                    ad_account_dict['name'] = ad_account.name
                    ad_account_dict['currency'] = ad_account.currency
                    ad_account_dict['timezone'] = ad_account.timezone

                    users_of_account = AdAccountUserJoinTable.objects.filter(ad_account_id = business_account.ad_account_id)
                    ad_account_users = []
                    for ad_account_user in users_of_account:
                        ad_account_user_dict = {}
                        user = User.objects.get(pk=ad_account_user.user_id)
                        ad_account_user_dict['firstname'] = user.firstname
                        ad_account_user_dict['lastname'] = user.lastname
                        ad_account_user_dict['email'] = user.email
                        ad_account_user_dict['current_role'] = AdAccount.getUserAccountRoleString(ad_account_user.current_role)
                        ad_account_users.append(ad_account_user_dict)
                    ad_account_dict['people'] = ad_account_users
                    ad_accounts.append(ad_account_dict)
                bm_dict['ad_accounts'] = ad_accounts

                people_and_assets.append(bm_dict)
            response_data['success'] = 'YES'
            response_data['data'] = people_and_assets
            response_data['total_count'] = len(people_and_assets)
        except Exception as e:
            response_data['success'] = 'NO'
            response_data['msg'] = str(e)

        return HttpResponse(json.dumps(response_data), content_type="application/json")
