from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.urls import reverse
from .models import Restaurant, Zona
from .forms import RestaurantForm, BuscarRestaurantForm, ActualizarRestaurantForm

def home(request):
  
    return HttpResponse(request, 'RestApp/home.html')

def agregar(request):
    '''
    TODO: agregar un mensaje en el template home.html que avise al usuario que 
    la persona fue cargada con éxito
    '''

    if request.method == "POST":
        form = RestaurantForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            direccion = form.cleaned_data['direccion']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            descripcion = form.cleaned_data['descripcion']
            Restaurant(nombre=nombre, direccion=direccion, email=email, telefono=telefono,descripcion=descripcion).save()

            return HttpResponseRedirect(reverse("home"))
    elif request.method == "GET":
        form = RestaurantForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    
    return render(request, 'RestApp/restaurant.html', {'form': form})

def Restaurant_borrar(request, identificador):
    '''
    TODO: agregar un mensaje en el template home.html que avise al usuario que 
    la persona fue eliminada con éxito        
    '''
    if request.method == "GET":
        restaurant = Restaurant.objects.filter(id=int(identificador)).first()
        if restaurant:
            restaurant.delete()
        return HttpResponseRedirect(reverse("home"))
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")
    
def actualizar(request, identificador=''):
    '''
    TODO: implementar una vista para actualización
    '''
    if request.method == "GET":
        restaurant = get_object_or_404(Restaurant, pk=int(identificador))
        initial = {
            "id": restaurant.id,
            "nombre": restaurant.nombre, 
            "direccion": restaurant.direccion, 
            "email": restaurant.email,
            "telefono": restaurant.telefono,
            "descripcion": restaurant.descripcion,
        }
    
        form_actualizar = ActualizarRestaurantForm(initial=initial)
        return render(request, 'RestApp/restaurant.html', {'form': form_actualizar, 'actualizar': True})
    
    elif request.method == "POST":
        form_actualizar = ActualizarRestaurantForm(request.POST)
        if form_actualizar.is_valid():
            Restaurant = get_object_or_404(Restaurant, pk=form_actualizar.cleaned_data['id'])
            restaurant.nombre= form_actualizar.cleaned_data['nombre']
            restaurant.direccion = form_actualizar.cleaned_data['direccion']
            restaurant.email = form_actualizar.cleaned_data['email']
            restaurant.telefono = form_actualizar.cleaned_data['telefono']
            restaurant.descripcion = form_actualizar.cleaned_data['descripcion']
            Restaurant.save()

            return HttpResponseRedirect(reverse("home"))
        
def Restaurant_buscar(request):
    
    if request.GET.get("palabra_a_buscar") and request.method == "GET":
        form_busqueda = BuscarRestaurantForm(request.GET)
        if form_busqueda.is_valid():
            restaurant = Restaurant.objects.filter(nombre__icontains=request.GET.get("palabra_a_buscar"))
            return  render(request, 'RestApp/restaurant.html', {"restaurant": restaurant, "resultados_busqueda":True})

    elif request.method == "GET":
        form_busqueda = BuscarRestaurantForm()
        return render(request, 'RestApp/restaurant.html', {"form_busqueda": form_busqueda})
    
def MostrarZona(request):
    
    zonas = Zona.objects.all()
    contexto={"zonas": zonas}
    
    return render(request, "RestApp/home.html", contexto)

