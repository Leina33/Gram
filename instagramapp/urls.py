from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home_images,name = 'home_images'),
]