from django.contrib.sites.models import Site
from django.shortcuts import render
from django.views import View

class MiVista(View):
    template_name = "mi_template.html"

    def get(self, request):
        params = {}
        current_site = Site.objects.get_current()
        params["dominio_actual"] = "https://" + current_site.domain
        return render(request, self.template_name, params)

