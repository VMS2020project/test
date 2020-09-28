"""API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('basepoint',views.apiOverview,name= 'basepoint'),
    path('basepointapi',views.apiWithRest,name='apiwithrest'),
    path('task-list',views.tasklist,name = 'task-list'),
    path('task-detail/<str:pk>/',views.taskdetail,name = 'task-detail'),
    path('task-create',views.taskcreate,name = 'task-create'),
    path('task-update/<str:pk>/',views.taskupdate,name = 'task-update'),
    path('task-delete/<str:pk>/',views.taskdelete,name = 'task-delete'),
    
]
