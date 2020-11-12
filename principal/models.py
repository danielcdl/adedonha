from django.contrib.auth import get_user_model
from django.db.models import Model
from django.db.models import CharField
from django.db.models import ForeignKey
from django.db.models import ManyToManyField
from django.db.models import EmailField
from django.db.models import BooleanField
from django.db.models import PositiveIntegerField
from django.db.models import CASCADE
from django.db.models import SET_NULL


class Tipo(Model):
    tipo = CharField(unique=True, max_length=100)

    def __str__(self):
        return self.tipo


class Palavras(Model):
    palavra = CharField(
        unique=True,
        max_length=100,
        null=False,
        blank=False
    )
    tipos = ManyToManyField(Tipo)

    def __str__(self):
        return self.palavra


class Jogador(Model):
    user = ForeignKey(get_user_model(), on_delete=CASCADE)
    nome = CharField(unique=True, max_length=100)
    email = EmailField(unique=True)

    def __str__(self):
        return self.nome


class Jogo(Model):
    jogo = CharField(unique=True, max_length=6, blank=False, null=False)
    ativo = BooleanField(default=False)
    tipo = ForeignKey(Tipo, on_delete=SET_NULL, blank=True, null=True, default=None)
    letra = CharField(max_length=1, blank=True, )
    ultima_letra = CharField(max_length=1, blank=True)
    palavra = CharField(max_length=100, blank=True)
    admin = ForeignKey(get_user_model(), on_delete=CASCADE)
    preferencias = ManyToManyField(Tipo, related_name='preferencias')

    def __str__(self):
        return self.jogo


class Jogos(Model):
    jogo = ForeignKey(Jogo, on_delete=CASCADE)
    jogador = ForeignKey(get_user_model(), on_delete=CASCADE)
    ordem = PositiveIntegerField()

    def __str__(self):
        return self.jogador


class PalavrasUsadas(Model):
    jogo = ForeignKey(Jogo, on_delete=CASCADE)
    palavra = ForeignKey(Palavras, on_delete=CASCADE)

    def __str__(self):
        return self.palavra
