from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# Vistas basadas en clase, la clase TemplateView ya contiene la lógica para renderizar una plantilla
class VistaInicio(TemplateView):
    template_name = 'inicio.html'

class VistaAbout(TemplateView):
    template_name = 'about.html'