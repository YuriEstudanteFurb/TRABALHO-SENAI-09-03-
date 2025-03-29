from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('paris', views.paris),
    path('oquefazer', views.oquefazer),
]




