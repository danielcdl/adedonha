from django.urls import path

from .views import Index, Palavras, Tipos

app_name = 'dados'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('tipos', Tipos.as_view(), name='tipos'),
    path('palavras', Palavras, name='palavras'),
]
