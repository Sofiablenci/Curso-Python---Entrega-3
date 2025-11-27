from django.urls import path

from inicio.views import vista, vista2, cargar_libro, listar_libros,ver_libro,ActualizarLibro,EliminarLibro
urlpatterns = [
    path('', vista, name='primeravista'),
    path('vista2/', vista2, name='segundavista'),
    path('ver-libro/<libro_id>/', ver_libro, name='ver'),
    path('actualizar-libro/<pk>/', ActualizarLibro.as_view(), name='actualizar'),
    path('eliminar-libro/<pk>/', EliminarLibro.as_view(), name='eliminar'),
    path('cargar-libro/', cargar_libro, name='cargar'),
    path('listado-libros/', listar_libros, name='listar')
]