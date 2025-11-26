from django.shortcuts import render
from django.views.generic import View
from django.views.generic import FormView
from contacto.models import Consulta
from contacto.forms import ConsultaForm
# Create your views here.

    
def preguntas_respuestas(request):
    params = {}
    params['nombre_sitio'] = 'Libros Online'
    return render(request, 'contacto/pregun_respues.html', params)