from django import forms


class CargarLibro(forms.Form):
    titulo = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=30)
    
    
class BuscarLibro(forms.Form):
    genero = forms.CharField(max_length=30, required=False)