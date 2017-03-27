from django.conf.urls import url, include
from rest_framework import routers
from user import views

urlpatterns = [
    url(r'^$', views.UserList.as_view()),
]
