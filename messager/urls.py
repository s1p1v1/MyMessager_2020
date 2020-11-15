"""my_messager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
#from django.contrib import admin
from django.urls import path
from messager.views import home, contacts, add_contact, send

app_name = 'messager'
urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('add_contact/', add_contact, name='add_contact'),
    #path('talk/', talk, name='talk'),
    #path('talk/<int:recipient_id>', talk, name='talk'),
    path('send/', send, name='send'),
    path('send/<int:recipient_id>', send, name='send'),
]
