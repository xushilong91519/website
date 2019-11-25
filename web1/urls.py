from django.urls import path
from . import views

app_name='web1'
urlpatterns=[
        path('',views.manage_order,name='manage_order'),
        path('<str:order_number>/',views.order_detail,name='order_detail'),
]
