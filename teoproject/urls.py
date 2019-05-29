"""teoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from rest_framework import routers
from teoapp import views

authors_list = views.AuthorsViewSet.as_view({'get':'list'})
authors_detail = views.AuthorsViewSet.as_view({'get':'retrieve'},lookup_field = 'nameId')
blog_topten = views.PostContentViewSet.as_view({'get':'list'})


urlpatterns = [

    path('admin/', admin.site.urls),
    path('stats/<str:nameId>/', authors_detail, name='author-detail'),
    path('stats/', blog_topten),
    path('authors/',authors_list)
    #path('', include('teoapp.urls')),
]
