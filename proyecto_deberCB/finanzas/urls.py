"""
    Manejo de urls para la aplicación
"""
from django.urls import path
# se importa las vistas de la aplicación
from finanzas import views


urlpatterns = [
        path('listar_coop', views.listar_coop, name='listar_coop'),
 ]