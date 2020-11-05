from random import choice

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import CreateView, ListView, UpdateView

from .forms import JogoForm, PalavrasUsadasForm, PalavrasForm, JogosForm, MudarDadosJogoForm, MudarUltimaLetraJogoForm, \
    NovoJogoForm, TipoForm
from .models import Jogos, PalavrasUsadas, Palavras, Jogo, Tipo


def dados(request):
    return render(request, "dados\\inicio.html")


def tipos(request):
    form = TipoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    dados_tipos = Tipo.objects.all()
    return render(request, "dados\\tipos.html", {'form': form, 'tipos': dados_tipos})


def criar_tipo(request):
    form = JogoForm(request.GET)
    return render(request, "principal\\index.html", {'form': form})


def atualizar_tipo(request):
    pass


def apagar_tipo(request):
    pass


def palavras(request):
    form = PalavrasForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    dados_palavras = Palavras.objects.all()
    return render(request, "dados\\palavras.html", {'form': form, 'palavras': dados_palavras})


def criar_palavra(request):
    pass


def atualizar_palavra(request):
    pass


def apagar_palavra(request):
    pass


@require_http_methods(["GET", "POST"])
def inicio(request):
    if request.method == 'POST':
        cod_jogo = request.POST.get('jogo')
        print('ok2')
        if Jogo.objects.filter(jogo=cod_jogo).last() is not None:
            print('ok3')
            jogadores = Jogos.objects.filter(jogo=get_object_or_404(Jogo, jogo=cod_jogo))
            nomes = []
            for dado in jogadores:
                nomes.append(dado.jogador.username)

            if request.user.username not in nomes:
                form = JogosForm()
                jogos = form.save(commit=False)
                jogos.jogo = get_object_or_404(Jogo, jogo=cod_jogo)
                jogos.jogador = request.user
                jogos.ordem = len(nomes) + 1
                jogos.save()

            return HttpResponseRedirect(reverse_lazy('principal:espera',
                                                     kwargs={
                                                         'jogo': cod_jogo
                                                     }
                                                     )
                                        )
        else:
            form = JogoForm(request.POST)
            return render(request,
                          "principal\\index.html",
                          {
                              'form': form,
                              'mensagem': f'O jogo {cod_jogo} não existe!'
                          }
                          )
    else:
        form = JogoForm(request.GET)
        return render(request, "principal\\index.html", {'form': form})


def novo_jogo(request):
    if request.method == 'POST':
        cod_jogo = ''
        caracteres = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'
        while len(cod_jogo) < 6:
            cod_jogo += choice(caracteres)

        form = NovoJogoForm()
        jogo = form.save(commit=False)
        jogo.jogo = cod_jogo
        jogo.admin = request.user
        jogo.save()

        jogadores = Jogos.objects.filter(jogo=get_object_or_404(Jogo, jogo=cod_jogo))
        nomes = []
        for dado in jogadores:
            nomes.append(dado.jogador.username)

        if request.user.username not in nomes:
            form = JogosForm()
            jogos = form.save(commit=False)
            jogos.jogo = get_object_or_404(Jogo, jogo=cod_jogo)
            jogos.jogador = request.user
            jogos.ordem = len(nomes) + 1
            jogos.save()

        return HttpResponseRedirect(reverse_lazy('principal:espera',
                                                 kwargs={
                                                     'jogo': cod_jogo
                                                 }
                                                 )
                                    )
    else:
        form = NovoJogoForm(request.GET)
        return render(request, "principal\\novo_jogo.html", {'form': form})


def espera(request, jogo):
    if request.method == 'GET':
        jogadores = Jogos.objects.filter(jogo=get_object_or_404(Jogo, jogo=jogo))
        nomes = []
        for dado in jogadores:
            nomes.append(dado.jogador.username)
        return render(
            request,
            'principal\\espera.html',
            {
                'jogadores': nomes,
                'jogo': jogo
            }
        )


def roleta(request, jogo):
    if request.method == 'POST':
        post_jogo = get_object_or_404(Jogo, jogo=jogo)
        form = MudarDadosJogoForm(request.POST, instance=post_jogo)
        if form.is_valid():
            dados_jogo = form.save(commit=False)
            dados_jogo.ativo = True
            dados_jogo.ultima_letra = request.POST['letra']
            dados_jogo.palavra = request.POST['letra']
            dados_jogo.save()

        return HttpResponseRedirect(reverse_lazy('principal:jogo', kwargs={'jogo': jogo}))
    # Qualquer outro método: GET, OPTION, DELETE, etc...
    else:
        form = MudarDadosJogoForm(request.GET)
        return render(request, "principal\\roleta.html", {'form': form, 'jogo': jogo})


def jogar(request, jogo):
    # Verificamos se o método POST
    if request.method == 'POST':
        post_jogo = get_object_or_404(Jogo, jogo=jogo)
        form = MudarUltimaLetraJogoForm(request.POST, instance=post_jogo)
        if form.is_valid():
            alterar_jogo = form.save(commit=False)
            alterar_jogo.palavra += alterar_jogo.ultima_letra
            alterar_jogo.save()
            return HttpResponseRedirect(reverse_lazy(
                'principal:espera',
                kwargs={'jogo': jogo}
            )
            )
    elif request.method == "GET":
        get_jogo = get_object_or_404(Jogo, jogo=jogo)
        form = MudarUltimaLetraJogoForm(request.GET, instance=get_jogo)
        return render(
            request,
            "principal\\jogo.html",
            {
                'form': form,
                'jogo': jogo,
                'palavra': get_jogo.palavra,
                'tipo': get_jogo.tipo,
                'letra': get_jogo.letra
            }
        )


class ResultadoListView(ListView):
    template_name = "principal/resultado.html"


class InserirCreateView(CreateView):
    template_name = "principal/inserir.html"
    model = Palavras
    form_class = PalavrasForm
    success_url = reverse_lazy("principal:inserir")


class DadosListView(ListView):
    template_name = "principal/listar.html"
    model = Palavras
    context_object_name = "dados"


class DadosUpdateView(UpdateView):
    template_name = "principal/atualizar.html"
    model = Palavras
    fields = '__all__'
    context_object_name = 'dado'
    success_url = reverse_lazy("principal:listar")
