from django.shortcuts import render
from productos.models import Producto
from django.http import Http404
from django.views.generic import View



class VerImagenes(View): 
    template = "tienda/verimagenes.html"

    def get(self, request):
        params={}
        try:
            productos = Producto.objects.all()
        except Producto.DoesNotExist:
            raise Http404
        params["productos"] = productos
        
        return render(request, self.template, params)

