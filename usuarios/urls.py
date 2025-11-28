from django.urls import path 
from usuarios.views import iniciar_sesion, registro
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('iniciar-sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('cerrar-sesion/', LogoutView.as_view(template_name='cerrar_sesion.html'), name='cerrar_sesion'),
    path('registro/', registro, name='registro'),
]
