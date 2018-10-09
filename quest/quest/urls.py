"""quest URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from sign import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    #登录处理
    path('login/',views.login),
    #登录成功的界面
    path('loginPage/',views.event_manage),
    path('search_name/',views.search_name),
    path('guestMange/',views.guest_manage),
    path('search_name_guest/',views.search_name_guest),
    url(r'^guestEvent/(?P<name>\d+)/$',views.guestEvent),
    path('logout/',views.logout),
    url(r'^sign_index/(?P<eid>\d+)/$',views.sign_index),
    url(r'^sign_index_action/(?P<eid>\d+)/$',views.sign_index_action),
    url(r'^add_guest/(?P<eid>\d+)/$', views.add_guest),
    url(r'^api/',include(('sign.urls','sign'),namespace="sign")),
]
