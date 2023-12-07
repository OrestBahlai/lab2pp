from django.conf.urls import url
from hardware_shop import views

urlpatterns=[
    url(r'^product$', views.productApi),
    url(r'^product/([0-9]+)$')
]