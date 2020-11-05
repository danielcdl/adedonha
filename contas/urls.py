from django.urls import path, include

from .views import Registro
app_name = 'principal'

urlpatterns = [
    path('registro/', Registro.as_view(), name='registro'),
]