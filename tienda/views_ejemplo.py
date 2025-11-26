from django.shortcuts import render
from productos.models import Producto
from django.db.models import Q
from django.http import Http404
from django.views.generic import View


class EjemploLocalSotage(View): 
    template = "tienda/localstorage.html"

    def get(self, request):
        params={}
        try:
            productos = Producto.objects.all()
        except Producto.DoesNotExist:
            raise Http404
        params["productos"] = productos
        # ##########################################################
        # PARA INICIALIZAR LA VARIABLE DE SESSION CARRO
        # ###########################################################
        try:
            request.session["carro"]
        except:
            request.session["carro"] = {}
        imagenes = list(Producto.objects.all())
        slides = [imagenes[i:i+5] for i in range(0, len(imagenes), 5)]    
        return render(request, self.template, {'slides': slides})
    