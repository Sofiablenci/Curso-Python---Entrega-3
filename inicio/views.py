from django.shortcuts import render
from django.http import HttpResponse
from inicio.models import Libro

def vista(request):
    #return HttpResponse('<h1>Bienvenido a la entrega 3</h1>')
    return render(request, 'vista.html')
    

def vista2(request):
    #return HttpResponse('<h1>Bienvenido a la entrega 3</h1>')
    return render(request, 'vista2.html')

def cargar_libro(request, titulo, genero):
    libro=Libro(titulo=titulo, genero=genero)
    libro.save()
    
    return render(request, 'cargar_libro.html', {'objeto_guardado': libro})

def listar_libros(request):
    
    libros= Libro.objects.all()
    return render(request, 'listar_libros.html', {'listado_de_libros': libros})