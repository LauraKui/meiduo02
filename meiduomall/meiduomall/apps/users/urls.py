
from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^register/$', views.Register.as_view(), name='register'),

]
