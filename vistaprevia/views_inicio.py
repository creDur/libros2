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

def index(request):
    params = {}
    params['nombre_sitio'] = 'Libros Online'
    producto=Producto.objects.filter( Q(estado="Publicado"), )
    params['producto']=producto
    print(producto)    
    #prod=ProductoME(nombre='Remera', descripcion='Esta es la descripción')
    #prod.save()

    return render(request, 'vistaprevia/index.html', params)
