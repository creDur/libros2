from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from Usuario.models import Datosusuario

@receiver(post_save, sender=User)
def create_datosusuario(sender, instance, created, **kwargs):
    if created:
        Datosusuario.objects.create(usuario=instance, nombre=instance)
        print("se han creado los datos adicionales de usuario")
		
@receiver(post_save, sender=User)
def update_datosusuario(sender, instance, created, **kwargs):
    if created==False:
        instance.datosusuario.save()
        print("se han creado los datos adicionales de usuario")