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
from sparkwebadmin.views import *
from  django.conf.urls.static import static
from  django.conf import settings

urlpatterns = [
    path('index/',index),
    path('about/',main5),
    path('slide/',main6),
    path('gallery/',main10),
    path('blogs/',main11),
    path('course1/',main9),
    path('contactus/',main4),
    path('review/',main7),
    path('deleterow6/<id>/',deleterow6),
    path('deleterow5/<id>/',deleterow5),
    path('deleterow4/<id>/',deleterow4),
    path('deleterow3/<id>/',deleterow3),
    path('deleterow8/<id>/',deleterow8),
    path('deleterow9/<id>/',deleterow9),
    path('deleterow10/<id>/',deleterow10),
    path('slideup/<id>/',slideup),
    path('testimonials/<id>/',testimonials),
    # path('contactup/<id>/',contactup),
    path('aboutup/<id>/',aboutup),
    path('course1up/<id>/',course1up),
    path('login/',login, name='login'),
    path('logout/',logout)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
