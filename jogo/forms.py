from django.forms import Form

from .models import Jogo


class JogoForm(Form):
    model = Jogo
    fields = '__all__'

class NovoJogoForm(Form):
    model = Jogo
    fields = '__all__'

class MudarDadosJogoForm(Form):
    model = Jogo
    fields = '__all__'

class MudarUltimaLetraJogoForm(Form):
    model = Jogo
    fields = '__all__'
