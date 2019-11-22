from django.urls import path
from . import views

app_name='web1'
urlpatterns=[
        path('',views.manage_post,name='manage_post'),
        path('detail/',views.post_detail,name='post_detail'),
]
