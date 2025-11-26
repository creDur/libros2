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
