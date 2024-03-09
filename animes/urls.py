from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='anime-home'),
    path('anime/<int:id>/', views.detail),
]
