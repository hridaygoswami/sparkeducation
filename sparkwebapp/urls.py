"""
URL configuration for sparkweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from sparkwebapp.views import *
from  django.conf.urls.static import static
from  django.conf import settings

urlpatterns = [
    path('index/', index),
    path('about/', about1),
    path('gallery/',gallery),
    path('blogs/',blogs),
    path('blogdetails/<int:id>/',blog_details),
    path('course/',course),
    path('coursedetails/<int:id>/',coursedetails),
    path('contact/',contact_page, name='contact-url'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
