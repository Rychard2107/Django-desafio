from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('anime/<int:id>/', views.anime),
]
