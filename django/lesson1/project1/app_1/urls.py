from django.urls import path
from . import views

urlpatterns = [
    path('1', views.url1),
    path('2', views.url2)
]
