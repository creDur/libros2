from django.urls import path
#from vistaprevia import views
from vistaprevia.views_ajax import para_ajax
from vistaprevia.views_buscar import BuscarLibro
from vistaprevia.views_buscar2 import BuscarLibro2
from vistaprevia.views_comedia import cuentos_com
from vistaprevia.views_cuentos import cuentos1
from vistaprevia.views_miedo import cuentos_mie
from vistaprevia.views_inicio import index
from vistaprevia.views_initial import secundario
from vistaprevia.views_templado import Templatetags1
from vistaprevia.views_templado2 import Templatetags2
from vistaprevia.views_templado import Templatetags1
from vistaprevia.views_templado import Templatetags1
from vistaprevia.views_templado2 import Templatetags2
from vistaprevia.views_tristesa import cuentos_tri

#from django.urls import path
#from vistaprevia import views
#from vistaprevia.views import Templatetags1
#from vistaprevia.views import Templatetags2
#from vistaprevia.views import BuscarLibro
#from vistaprevia.views import BuscarLibro2

urlpatterns = [
    path('', index, name='home'),
    #path('templatetags1', Templatetags1.as_view(), name='templatetags1'),    
    #path('index_tem', Templatetags2.as_view(), name='index_tem'),    
    path('templatetags1', Templatetags1.as_view(), name='templatetags1'),    
    path('index_tem', Templatetags2.as_view(), name='index_tem'),   
    path('second_inx', secundario, name='sec_index'),
    path('cuentos', cuentos1, name='cuentos'),
    path('cuentos_comicos', cuentos_com, name='cuentos_com'),
    path('cuentos_miedo', cuentos_mie, name='cuentos_mie'),
    path('cuentos_tristesa', cuentos_tri, name='cuentos_tri'),
    path("usar_ajax", para_ajax,  name="usar_ajax"),
    path("buscar_libro/", BuscarLibro.as_view(), name="buscar_libro"),
    path("buscar_libro2/", BuscarLibro2.as_view(), name="buscar_libro2"),
]