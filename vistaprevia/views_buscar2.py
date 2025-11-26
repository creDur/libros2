from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from productos.models import Producto
from django.views.generic import View
import datetime
from django.shortcuts import redirect
from datetime import datetime
import mimetypes
from productos.forms import SearchLibroForm
import json
from django.shortcuts import HttpResponse
"""************************************************************************************
* PASO 3 LO IMPORTO
************************************************************************************"""
from vistaprevia.models import ProductoME
"""
def index(request):
    return HttpResponse("Hola Mundo!")
"""
"""**********************************************************
* PRIMERA FORMA MEDIANTE PyMongo 
* PASO 1 - IMPORTO
**********************************************************"""
from vistaprevia.utils import get_db_handle 



class BuscarLibro(View):

    def is_ajax(self, request):
        return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

    def get(self, request):
        if self.is_ajax(request=request):

            palabra=request.GET.get('term', '')
            print(palabra)
            libro=Producto.objects.filter(producto__icontains=palabra)
            result=[]
            for an in libro:
                data={}
                data['label']=an.producto
                result.append(data)
            data_json=json.dumps(result)
        else:
            data_json="fallo"
        mimetype="application/json"
        return HttpResponse(data_json, mimetype)



class BuscarLibro2(View):

    def is_ajax(self, request):
        return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

    def get(self, request):
        if self.is_ajax(request=request):
            q = request.GET['valor']
            libro = Producto.objects.filter(producto__icontains=q)
            results = []
            for rec in libro:
                #print(rec.producto)
                #print(rec.imagen)
                #print(rec.usuario)

                #print(rec.fecha_nacimiento)
                data = {}
                data['producto'] = rec.producto
                data['ruta_imagen'] = str(rec.imagen)
                data['usuario'] = rec.usuario
                data['fecha_nacimiento'] = str(rec.fecha_nacimiento)
                data['nombre'] = rec.nombre
                data['descripcion'] = rec.descripcion
                results.append(data)
            data_json = json.dumps(results)

        else:
            data_json = "fallo"
        mimetype = "application/json"
        return HttpResponse(data_json, mimetype)