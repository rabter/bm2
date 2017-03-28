from django.conf.urls import url, include
from rest_framework import routers
from business_manager import views

urlpatterns = [
    url(r'^$', views.BusinessManagerList.as_view()),
    url(r'^business_info/$', views.PeopleAndAssetList.as_view()),
]
