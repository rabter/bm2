from django.shortcuts import render
from django.http import HttpResponse
from user.models import User
from user.serializers import UserSerializer
from rest_framework.views import APIView
import json

class UserList(APIView):

    def get(self, request, format=None):
        response_data = {}
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        response_data['data'] = serializer.data
        return HttpResponse(json.dumps(response_data), content_type="application/json")
