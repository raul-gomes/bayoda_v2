from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'babyoda'

urlpatterns = [
    path('', views.home, name='home'),
    path('evento/', views.evento, name='evento'),
    path('galeria/', views.galeria, name='galeria'),
    path('mensagens/', views.mensagens, name='mensagens'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)