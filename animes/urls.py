from django.urls import path
from . import views

app_name = 'animes'


urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/genero/<int:genero_id>/', views.genero, name="genero"),
    path('recipes/create/', views.create_anime, name="create"),
    path('anime/<int:id>/', views.detail),
]
