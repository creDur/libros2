from django.db import models
from django.utils.html import format_html

class Categoria(models.Model):
    nombre1 = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return '%s' % self.nombre1


class Producto(models.Model):

    Borrador = 'Borrador'
    PUBLICADO = 'Publicado'
    Retirado = 'Retirado'
    APROBACION_PRODUCTO = (
        (Borrador, 'Borrador'),
        (PUBLICADO, 'Publicado'),
        (Retirado, 'Retirado'),
    )
    estado = models.CharField(max_length=10, choices=APROBACION_PRODUCTO, blank=True,default=PUBLICADO)

    producto = models.CharField(max_length=200)
    usuario = models.CharField(max_length=20)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    dni = models.CharField(max_length=10)
    lugar_pais = models.CharField(max_length=30)
    lugar_ciudad = models.CharField(max_length=30)
    contrasena= models.CharField(max_length=15, null=True)    
    fecha_nacimiento = models.DateTimeField('Fecha de nacimiento')
    imagen = models.ImageField(upload_to="productos/", blank=True, null=True) 
    images = models.ImageField(upload_to="producto/%Y/%m/%d", blank=True, null=True) 

    stock = models.IntegerField(default=0)
    descripcion = models.TextField(default="")
    precio= models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    descuento =models.IntegerField(default=0)

    categoria = models.ForeignKey(
        Categoria, blank=False, null=True, on_delete=models.CASCADE
    )


    def tipo_de_producto(self):
        if self.estado == "Retirado":
            return format_html(
                '<span style="color: #f00;">{}</span>', 
                self.estado,
                  )
        elif self.estado == "Borrador":
            return format_html(
                '<span style="background-color: #f0f; padding:7px;">{}</span>', 
                self.estado, 
                )
        elif self.estado == 'Publicado':
            return format_html(
            '<span style="background-color:#FOB203; color:#000; padding:5px;">{}</span>', 
            self.estado,
              )
    def __str__(
        self,
    ):
        return self.producto + "---" + str(self.fecha_nacimiento)
    
    def get_absolute_url(self):
        return f"/ver//{self.producto}/"