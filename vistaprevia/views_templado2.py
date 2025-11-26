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


class Templatetags2(View):
    template = "vistaprevia/index_tem.html"
    def get(self, request):
        params = {}
        params["cross_site_scripting"]="""
            <script>
            $("*").css({
                "background-color": "yellow",
                "font-weight": "bolder",
            });
            </script>
        
        """
        producto = Producto.objects.filter(
            Q(estado="Publicado"),
        )
        params["los_productos"]=producto
        params['fecha_de_hoy']=datetime.datetime.now()
        params['mi_lista']=[1,2,3,4,5,6,7,8,9]
        params['colum3']='colum3'
        params['mi_lista2']=[]
        return render(request, self.template, params)
    def post(self, request):
        params = {}
        producto=request.POST.get("producto")
        el_pedido =request.session.get("el_pedido")
        if el_pedido:
            cantidad= el_pedido.get(producto)
            if cantidad:
                el_pedido[producto]=cantidad+1
            else:
                el_pedido[producto]=1
        else:
            el_pedido={}
            el_pedido[producto]=1
 
        request.session["el_pedido"]=el_pedido
        print(request.session["el_pedido"])

        return redirect("index_tem")
    
