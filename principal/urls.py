from django.urls import path

from .views import dados, criar_tipo, atualizar_tipo, apagar_tipo, criar_palavra, atualizar_palavra, apagar_palavra, \
    tipos, palavras, inicio, roleta, jogar, ResultadoListView, espera, novo_jogo

app_name = 'principal'

urlpatterns = [
    path('', inicio, name='index'),

    path('dados', dados, name='dados'),

    path('dados/tipos', tipos, name='tipos'),
    path('dados/criar-tipo', criar_tipo, name='criar_tipo'),
    path('dados/atualizar-tipo', atualizar_tipo, name='atualizar_tipo'),
    path('dados/apagar-tipo', apagar_tipo, name='apagar_tipo'),

    path('dados/palavras', palavras, name='palavras'),
    path('dados/criar-palavra', criar_palavra, name='criar_palavra'),
    path('dados/atualizar-palavra', atualizar_palavra, name='atualizar_palavra'),
    path('dados/apagar-palavra', apagar_palavra, name='apagar_palavra'),

    path('novo-jogo', novo_jogo, name='novo-jogo'),
    path('espera/<jogo>', espera, name='espera'),
    path('roleta/<jogo>', roleta, name='roleta'),
    path('jogo/<jogo>', jogar, name='jogo'),
    path('resultado', ResultadoListView.as_view, name='resultado'),
]
