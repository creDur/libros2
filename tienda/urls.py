from django.urls import path
from tienda import views_agregar
from tienda.views_verimagenes import VerImagenes
from tienda.views_verimagen import ver_imagen
from tienda.views_ejemplo import EjemploLocalSotage
from tienda.views_cargar import cargar_imagen


urlpatterns = [
    path('cargar/', cargar_imagen, name="cargar"),
    path('tienda/ver/<int:producto_id>', ver_imagen, name="ver"),  
    path('verimagenes/', VerImagenes.as_view(), name="verimagenes"),
    path('ejemplo_localstorage/', EjemploLocalSotage.as_view(), name="ejemplo_localstorage"),
    path("agregar/", views_agregar.agregar, name="agregar"),

]