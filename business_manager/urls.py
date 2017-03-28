from django.conf.urls import url, include
from rest_framework import routers
from business_manager import views

urlpatterns = [
    url(r'^$', views.BusinessManagerList.as_view()),
]
