from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('nossahistoria/', views.nossahistoria, name="nossahistoria"),
    path('listadepresente/', views.listadepresente, name="listadepresente"),
    path('trajes/', views.trajes, name="trajes"),
]
