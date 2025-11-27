from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Libro
from inicio.forms import CargarLibro, BuscarLibro
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

def vista(request):
    #return HttpResponse('<h1>Bienvenido a la entrega 3</h1>')
    return render(request, 'vista.html')
    

def vista2(request):
    #return HttpResponse('<h1>Bienvenido a la entrega 3</h1>')
    return render(request, 'vista2.html')

def cargar_libro(request):
    
    if request.method == 'POST':
        formulario=CargarLibro(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            
            libro=Libro(titulo=info.get('titulo'), genero=info.get('genero'))
            libro.save()
            
            return redirect('listar')
    else:
        formulario=CargarLibro()
    return render(request, 'cargar_libro.html', {'formulario': formulario})

def listar_libros(request):
    formulario= BuscarLibro(request.GET)
    if formulario.is_valid():
        genero_a_buscar= formulario.cleaned_data.get('genero')
        listado_de_libros=Libro.objects.filter(genero__icontains=genero_a_buscar)
        
    return render(request, 'listar_libros.html', {'listado_de_libros': listado_de_libros, 'formulario': formulario})

def ver_libro(request, libro_id):
    libro = Libro.objects.get(id=libro_id)
    return render(request, 'ver_libro.html', {'libro': libro}) 


class ActualizarLibro(UpdateView):
    model = Libro
    template_name= 'actualizar_libro.html'
    fields = '__all__'
    success_url = reverse_lazy('listar')
    
class EliminarLibro(DeleteView):
    model = Libro
    template_name= 'eliminar_libro.html'
    success_url = reverse_lazy('listar')