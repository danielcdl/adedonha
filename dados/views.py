from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.base import TemplateView

from .models import Tipo
from .models import Palavra

from .forms import TipoForm
from .forms import PalavraForm


class Index(TemplateView):
    template_name = "dados/inicio.html"


class Tipos(View):
    template_name = "dados/tipos.html"
    form = TipoForm()
    context = {}

    def get(self, request):
        self.context['form'] = self.form
        self.context['tipos'] = Tipo.objects.all()

        return render(request, self.template_name, self.context)

    def post(self, request):
        form = TipoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, self.template_name, self.context)
        else:
            return render(request, self.template_name, {'form': form})


class Palavras(View):
    template_name = "dados/palavras.html"
    form = PalavraForm()
    context = {}

    def get(self, request):
        self.context['form'] = self.form
        self.context['palavras'] = Palavra.objects.all()
        return render(request, self.template_name, self.context)

    def post(self, request):
        form = PalavraForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, self.template_name, self.context)
        else:
            return render(request, self.template_name, form)
