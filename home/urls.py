from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('imovel/<str:id>', views.real_estate, name="imovel"),
    path('agendar_visitas', views.schendule_visit, name="agendar_visitas"),
    path('agendamentos', views.schenduling, name="agendamentos"),
    path('cancelar_agendamento/<str:id>', views.removed_scheduling, name="cancelar_agendamento")
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
