"""articlesapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import UserCreateAPIView, UserListAPIView, ProfileAPIView
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    url(r'^auth/', include('rest_framework.urls')),
    url(r'^api/auth/login/$', ObtainAuthToken.as_view()),
    url(r'^api/users/create/$', UserCreateAPIView.as_view()),
    url(r'^accounts/profile/$', ProfileAPIView.as_view()),
    url(r'^api/users/$', UserListAPIView.as_view()),
    url(r'^api/articles/', include('articles.urls')),
]
