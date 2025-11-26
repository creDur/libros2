from django.shortcuts import render
#from django.http import HttpResponse
from django.contrib.auth import logout

"""
def index(request):
    return HttpResponse("Hola Mundo!")
"""
def pagina_logout_adios(request):
    params = {}
    logout(request)
    return render(request, 'Usuario/logout_adios.html', params)
