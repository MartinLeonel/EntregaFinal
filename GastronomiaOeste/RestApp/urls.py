from django.urls import path
from RestApp import views


urlpatterns = [
    path('', views.MostrarZona, name="home"),
    path('restaurant/', views.agregar, name="restaurant"),
    path('Moron/', views.agregar, name="Moron"),
    path('restaurant/', views.agregar, name="restaurant"),
    path('restaurant/', views.agregar, name="restaurant"),
    path('restaurant/', views.agregar, name="restaurant"),
    path('restaurant/', views.agregar, name="restaurant")
]