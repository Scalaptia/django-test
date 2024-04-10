from django.urls import path
from .views import VistaInicio, VistaAbout

urlpatterns = [
    path('', VistaInicio.as_view(), name='inicio'),
    path('about/', VistaAbout.as_view(), name='about'),
]