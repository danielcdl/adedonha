from django import forms
from .models import Jogos, PalavrasUsadas, Palavras, Jogo, Tipo


class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = '__all__'

class PalavrasForm(forms.ModelForm):
    class Meta:
        model = Palavras
        fields = ['palavra', 'tipos']

class JogosForm(forms.ModelForm):
    class Meta:
        model = Jogos
        fields = ['jogo']

class JogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = ['jogo']


class NovoJogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = ['preferencias']

class MudarDadosJogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = ['tipo','letra']


class MudarUltimaLetraJogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = ['ultima_letra']

class PalavrasUsadasForm(forms.ModelForm):
    class Meta:
        model = PalavrasUsadas
        fields = '__all__'


