from django.shortcuts import render
#from django.http import HttpResponse
from productos.models import Producto
from django.views.generic import View
from django.http import Http404

"""
def index(request):
    return HttpResponse("Hola Mundo!")  
params['nombre_sitio'] = 'Libros Online'

"""
class TomaUsu(View): 
    template = "vistaprevia/perfil.html"

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
        perfile = list(Producto.objects.all())
 
        return render(request, self.template, {'perfile': perfile})



