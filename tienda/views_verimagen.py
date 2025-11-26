from django.shortcuts import render
from productos.models import Producto
from django.http import Http404

def ver_imagen(request, producto_id):
    params={}
    try:
        producto = Producto.objects.get(pk=producto_id)
    except Producto.DoesNotExist:
        raise Http404
    params["producto"] = producto
    
    return render(request, "tienda/verimagen.html", params)

