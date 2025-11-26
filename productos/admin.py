# Register your models here.
from django.contrib import admin
from productos.models import Categoria
from productos.models import Producto
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
class ProductoInline(admin.TabularInline):

    model = Producto
    extra = 0

class CategoriaAdmin(admin.ModelAdmin):
    inlines = [ProductoInline]




@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Relación", {"fields": ["categoria"]}),
        (
            "Datos generales",
            {
                "fields": [
                   'producto', 'estado', 'fecha_nacimiento', 'usuario', 'imagen', 'nombre', 'apellido', 'email', 'dni', 'lugar_pais', 'lugar_ciudad', 'contrasena', 'descripcion'
                ]
            },
        ),
     (
            "Datos económicos",
            {
                "fields": [
                   'stock', 'precio', 'descuento'
                ]
            },
        ),
    ]
    list_display = ['usuario', 'estado','fecha_nacimiento', 'imagen', 'nombre', 'apellido', 'email', 'dni', 'lugar_pais', 'lugar_ciudad', 'contrasena', 'producto', 'stock', 'descripcion', 'precio', 'descuento']
    ordering = ['-fecha_nacimiento']
    list_filter = ('usuario', 'fecha_nacimiento',)
    search_fields=('usuario', 'nombre',)
    list_display_links = ('usuario', 'fecha_nacimiento')
    actions=['publicar', 'exportar_a_json', 'ver_productos']

    def publicar(self, request, queryset):
        registro = queryset.update(estado= "Publicado")

        if registro == 1:
            mensaje = "1 registro actualizado"
        else:
            mensaje = "%s registros actualiazados" % registro
        self.message_user(request, "%s exitosamente" % mensaje)
    
    publicar.short_description = "Pasar a publicado"

    def exportar_a_json(self, request, queyset):
        response = HttpResponse(content_type="application/json")
        serializers.serialize("json", queyset, stream=response)
        return response
    
    def ver_productos(self, request, queyset):
        params={}
        productos= Producto.objects.all()
        params["productos"]=productos
        return render(request, "admin/productos/productos.html", params)
    
    ver_productos.short_description = "ver productos"

admin.site.register(Categoria, CategoriaAdmin)




