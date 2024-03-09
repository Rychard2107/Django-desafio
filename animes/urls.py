from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'animes'


urlpatterns = [
    path('', views.home, name="home"),
    path('animes/genero/<int:genero_id>/', views.genero, name="genero"),
    path('animes/create/', views.create_anime, name="create"),
    path('<int:id>/', views.detail, name='detail'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
