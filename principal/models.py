from django.contrib.auth import get_user_model
from django.db import models

class UpperCharField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(UpperCharField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).upper()

class Tipo(models.Model):
    tipo = UpperCharField(unique=True,max_length=100)

    def __str__(self):
        return self.tipo


class Palavras(models.Model):
    palavra = UpperCharField(
        unique=True,
        max_length=100,
        null=False,
        blank=False
    )
    tipos = models.ManyToManyField(Tipo)

    def __str__(self):
        return self.palavra


class Jogador(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    nome = UpperCharField(unique=True, max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome


class Jogo(models.Model):
    jogo = UpperCharField(unique=True, max_length=6, blank=False, null=False)
    ativo = models.BooleanField(default=False)
    tipo = models.ForeignKey(Tipo, on_delete=models.SET_DEFAULT, blank=True, null=True,default=None)
    letra = UpperCharField(max_length=1, blank=True,)
    ultima_letra = UpperCharField(max_length=1, blank=True)
    palavra = UpperCharField(max_length=100, blank=True)
    admin = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    preferencias = models.ManyToManyField(Tipo, related_name='preferencias')

    def __str__(self):
        return self.jogo


class Jogos(models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    jogador = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    ordem = models.IntegerField()

    def __str__(self):
        return self.jogador


class PalavrasUsadas(models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    palavra = models.ForeignKey(Palavras, on_delete=models.CASCADE)

    def __str__(self):
        return self.palavra
