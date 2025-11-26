from django.shortcuts import render
#from django.http import HttpResponse
"""
def index(request):
    return HttpResponse("Hola Mundo!")
"""
def pagina_logout(request):
    params = {}
    return render(request, 'Usuario/logout.html', params)
