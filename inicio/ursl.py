from django.urls import path

from inicio.views import vista, vista2, cargar_libro, listar_libros
urlpatterns = [
    path('', vista),
    path('vista2/', vista2),
    path('cargar-libro/<titulo>/<genero>/', cargar_libro),
    path('listado-libros/', listar_libros)
]