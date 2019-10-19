"""mediabias URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from predict.views import predictpage,url_list,parse,parseclicked,index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^predict/', predictpage),
    url(r'^urls/', url_list),
    url(r'^feed/', parse),
    url(r'^feed1/', parse1),
    url(r'^feed2/', parse2),
    url(r'^feed3/', parse3),
    url(r'^feed4/', parse4),
    url(r'^url/(?P<id>\d+)/$', parseclicked),
    url(r'^$', index),
]
