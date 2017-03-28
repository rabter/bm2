from django.conf.urls import url, include
from rest_framework import routers
from ad_account import views

urlpatterns = [
    url(r'^$', views.AdAccountList.as_view()),
]
