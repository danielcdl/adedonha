from django.urls import path

from .views import Index, NovoJogo, Jogar, Espera, Resultado, Roleta

app_name = 'jogo'

urlpatterns = [
    path('', Index, name='index'),
    path('novo-jogo', NovoJogo.as_view(), name='novo-jogo'),
    path('espera/<jogo>', Espera.as_view(), name='espera'),
    path('roleta/<jogo>', Roleta.as_view(), name='roleta'),
    path('jogo/<jogo>', Jogar.as_view(), name='jogo'),
    path('resultado', Resultado.as_view(), name='resultado'),
]
