"""mysite URL Configuration

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

from django.urls import path, include
from .views import posts_list,post_detail,PostCreate,PostUpdate,PostDelete
from django.views.generic import ListView, DetailView
from diary.models import Articles


urlpatterns = [
    path('', posts_list, name='post_list_url'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/update/', PostUpdate.as_view(), name='post_update_url'),
    path('post/<str:slug>/delete/', PostDelete.as_view(), name='post_delete_url'),
    path('post/<str:slug>/', post_detail, name='post_detail_url')
    
    # {% url'post_list_url' %}
]
