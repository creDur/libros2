from django.urls import path
#from contacto import views
from contacto.views_contacto import Contacto
#from contacto.views import Contacto, MensajeEnviado, preguntas_respuestas
from contacto.views_enviado import MensajeEnviado
from contacto.views_qa import preguntas_respuestas

urlpatterns = [
    path("", Contacto.as_view(), name="contacto"),
    path("mensaje_enviado", MensajeEnviado.as_view(), name="mensaje_enviado"),
    path("preg_resp", preguntas_respuestas, name="preg_resp"),

]
