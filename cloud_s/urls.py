from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='cloud_s'),
    path('add-cloud_s', views.add_cloud_s, name='add-cloud_s')
]
