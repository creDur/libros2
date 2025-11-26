from django.shortcuts import render
from django.shortcuts import redirect
from productos.models import Producto
from tienda.forms import CargarForm



def cargar_imagen(request):
    params={}

    if request.method == 'POST':
        form = CargarForm(request.POST, request.FILES)
        params['form']=form
        if form.is_valid():
            producto = form.cleaned_data['producto']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            imagen = form.cleaned_data['imagen']

            nuevo_producto = Producto(producto=producto, fecha_nacimiento=fecha_nacimiento, imagen=imagen)
            nuevo_producto.save()
            return redirect('index')

    else:
        form = CargarForm()
        params['form'] = form
        return render(request, 'tienda/formulario.html', params)

