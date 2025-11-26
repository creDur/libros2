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



def secundario(request):
    params = {}
    params['nombre_sitio'] = 'Libros Online'
    producto=Producto.objects.filter( Q(estado="Publicado"), )
    params['producto']=producto
    print(producto)
    return render(request, 'vistaprevia/second_inx.html', params)


def cuentos1(request):
    params = {}
    params['nombre_sitio'] = 'Libros Online'
    return render(request, 'vistaprevia/cuentos.html', params)

def cuentos_com(request):
    params = {}
    params['nombre_sitio'] = 'Libros Online'
    titulo=Producto.objects.all()
    params['titulo']=titulo
    print(titulo)
    return render(request, 'vistaprevia/cuentos_comicos.html', {'titulo': titulo})

def cuentos_mie(request):
    params = {}
    params['nombre_sitio'] = 'Libros Online'
    titulo=Producto.objects.all()
    params['titulo']=titulo
    print(titulo)
    return render(request, 'vistaprevia/cuentos_miedo.html', {'titulo': titulo})

def cuentos_tri(request):
    params = {}
    params['nombre_sitio'] = 'Libros Online'
    titulo=Producto.objects.all()
    params['titulo']=titulo
    print(titulo)
    return render(request, 'vistaprevia/cuentos_tristesa.html', {'titulo': titulo})

class Templatetags1(View):
    template = "vistaprevia/templatetags1.html"
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

        return redirect("templatetags1")
    
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
    

def para_ajax(request):
    params={}
    search=SearchLibroForm()
    params['search']=search
    return render(request, 'vistaprevia/ver_ajax.html', params)



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