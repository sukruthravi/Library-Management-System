"""ProTwo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

# from django.conf.urls import url,include
from AppTwo import views

urlpatterns = [
    #this is the main index.html page, from here the control this transfered to views file in AppTwo and then to index function
    path('', views.index, name='index'),
    # url(r'^$',vies.index, name='index'),
    #when you use include, the control is transfered to url.py file in AppTwo and then from there to views.py file
    #after / if help comes then help is called else if users come then users is called.
    path('apptwo/', include('AppTwo.urls')),
    path('logout/',views.user_logout,name='logout'),
    path('admin/', admin.site.urls),
]
