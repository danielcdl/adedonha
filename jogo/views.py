from random import choice

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views.generic.base import View

from .forms import JogoForm
from .forms import NovoJogoForm
from .forms import MudarDadosJogoForm
from .forms import MudarUltimaLetraJogoForm

from .models import Jogo


class Index(View):
    template_name = "jogo/index.html"
    form = JogoForm()
    context = {}

    def get(self, request):
        self.context['form'] = self.form
        return render(request, self.template_name, self.context)

    def post(self, request):
        cod_jogo = request.POST.get('jogo')
        jogo = Jogo.objects.filter(jogo=cod_jogo).last()
        if jogo is not None:
            jogadores = Jogo.objects.filter(jogo=jogo)
            nomes = []
            for jogador in jogadores:
                nomes.append(jogador.jogador.username)

            if request.user.username not in nomes:
                form = JogoForm()
                jogos = form.save(commit=False)
                jogos.jogo = get_object_or_404(Jogo, cod_jogo)
                jogos.jogador = request.user
                jogos.ordem = len(nomes) + 1
                jogos.save()

            return redirect('principal:espera', jogo=cod_jogo)
        else:
            form = JogoForm(request.POST)
            self.context['form'] = form
            self.context['mensagem'] = f'O jogo {cod_jogo} não existe!'
            return render(request, self.template_name, self.context)


class NovoJogo(View):
    template_name = 'principal/novo_jogo.html'
    form = NovoJogoForm()
    context = {}

    def get(self, request):
        self.context['form'] = self.form

        return render(request, self.template_name, self.context)

    def post(self, request):
        cod_jogo = ''
        caracteres = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'
        while len(cod_jogo) < 6:
            cod_jogo += choice(caracteres)

        jogo = self.form.save(commit=False)
        jogo.jogo = cod_jogo
        jogo.admin = request.user
        jogo.save()

        jogadores = Jogo.objects.filter(jogo=cod_jogo)
        nomes = []
        for dado in jogadores:
            nomes.append(dado.jogador.username)

        if request.user.username not in nomes:
            jogos = self.form.save(commit=False)
            jogos.jogo = get_object_or_404(Jogo, jogo=cod_jogo)
            jogos.jogador = request.user
            jogos.ordem = len(nomes) + 1
            jogos.save()

        return redirect('principal:espera', jogo=cod_jogo)


class Espera(View):
    template_name = 'principal/espera.html'
    context = {}

    def get(self, request):
        jogo = request.GET.get('jogo')
        jogadores = Jogo.objects.filter(jogo=jogo)
        nomes = []
        for dado in jogadores:
            nomes.append(dado.jogador.username)
        self.context['jogadores'] = nomes
        self.context['jogo'] = jogo
        return render(request, self.template_name, self.context)


class Roleta(View):
    template_name = 'principal/roleta.html'
    form = MudarDadosJogoForm()
    context = {}

    def get(self, request):
        jogo = request.GET.get('jogo')
        self.context['form'] = self.form
        self.context['jogo'] = jogo
        return render(request, self.template_name, self.context)

    def post(self, request):
        jogo = request.GET.get('jogo')
        post_jogo = get_object_or_404(Jogo, jogo=jogo)
        form = MudarDadosJogoForm(request.POST, instance=post_jogo)
        if form.is_valid():
            dados_jogo = form.save(commit=False)
            dados_jogo.ativo = True
            dados_jogo.ultima_letra = request.POST['letra']
            dados_jogo.palavra = request.POST['letra']
            dados_jogo.save()

        return redirect('principal:jogo', jogo=jogo)


class Jogar(View):
    template_name = 'principal/jogo.html'
    context = {}

    def get(self, request):
        jogo = request.GET.get('jogo')
        get_jogo = get_object_or_404(Jogo, jogo=jogo)
        form = MudarUltimaLetraJogoForm(request.GET, instance=get_jogo)
        self.context['form'] = form,
        self.context['jogo'] = jogo,
        self.context['palavra'] = get_jogo.palavra,
        self.context['tipo'] = get_jogo.tipo,
        self.context['letra'] = get_jogo.letra
        return render(request, self.template_name, self.context)

    def post(self, request):
        jogo = request.GET.get('jogo')
        post_jogo = get_object_or_404(Jogo, jogo=jogo)
        form = MudarUltimaLetraJogoForm(request.POST, instance=post_jogo)
        if form.is_valid():
            alterar_jogo = form.save(commit=False)
            alterar_jogo.palavra += alterar_jogo.ultima_letra
            alterar_jogo.save()
            return redirect('principal:espera', jogo=jogo)


class Resultado(ListView):
    template_name = "principal/resultado.html"
