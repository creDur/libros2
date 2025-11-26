from django.urls import path
from vistaprevia import views
from Usuario import views_login
from Usuario import views_logout
from Usuario import views_logout_adios
from Usuario import views_registro
#from Usuario.views_dominio import MiVista

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views_login.pagina_login, name='login'),
    path('logout',  views_logout.pagina_logout, name='logout'),
    path('logout_adios', views_logout_adios.pagina_logout_adios, name='logout_adios'),
    path('registro', views_registro.pagina_registro, name='registro'),
   # path("registro", MiVista.as_view(), name="mi_vista"),
]