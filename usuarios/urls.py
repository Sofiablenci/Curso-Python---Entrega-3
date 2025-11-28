from django.urls import path 
from usuarios.views import iniciar_sesion

urlpatterns = [
    path('iniciar-sesion/', iniciar_sesion, name='iniciar_sesion')
    
]
