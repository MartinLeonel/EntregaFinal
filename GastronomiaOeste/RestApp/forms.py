from email.policy import default
from django import forms

class RestaurantForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    direccion = forms.CharField(label="direccion", max_length=100)
    email = forms.EmailField(label="Email")
    telefono = forms.IntegerField(label="Telefono")
    descripcion = forms.CharField(label="descripcion")

class ActualizarRestaurantForm(RestaurantForm):
    id = forms.IntegerField(widget = forms.HiddenInput())


class BuscarRestaurantForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")
    
class Carta(forms.Form):
    plato = forms.CharField(label="Plato", max_length=100)
    precio = forms.FloatField(label="Precio")
    descripcion = forms.CharField(label="Descripcion", max_length=100)