"""website URL Configuration

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
from django.urls import include,path
from web1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.manage_order),
    path('order/',include('web1.urls')),
    path('add_order/',views.add_order),
    path('submit_order/<str:order_number>/',views.submit_order),
    path('edit_order/<str:order_number>/',views.edit_order),
    path('container/<str:container_number>/',views.container_detail),
]
