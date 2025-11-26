from django.shortcuts import render
from django.views.generic import View
from django.views.generic import FormView
from contacto.models import Consulta
from contacto.forms import ConsultaForm
# Create your views here.


class MensajeEnviado(View):
    template= 'contacto/mensaje_enviado.html'
    def get(self, request):
        params = {}
        params['mensaje'] = 'aqui va un mensaje'
        return render(request, self.template, params)
    
