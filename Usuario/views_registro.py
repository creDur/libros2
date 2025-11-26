from django.shortcuts import render
from django.shortcuts import redirect
from Usuario.forms import CreateUserForm
#from django.http import HttpResponse
"""
def index(request):
    return HttpResponse("Hola Mundo!")
"""
def pagina_registro(request):
    params = {}
    form= CreateUserForm()
    params["form"]= form
    # dominio actual con http/https incluido
    #dominio_actual = request.scheme + "://" + request.get_host()
    #params["dominio_actual"] = dominio_actual
    if request.method == "POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    return render(request, 'Usuario/registro.html', params)

