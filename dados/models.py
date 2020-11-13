from django.db.models import Model
from django.db.models import CharField
from django.db.models import ManyToManyField

class Tipo(Model):
    tipo = CharField(unique=True, max_length=100)

    def __str__(self):
        return self.tipo


class Palavra(Model):
    palavra = CharField(
        unique=True,
        max_length=100,
        null=False,
        blank=False
    )
    tipos = ManyToManyField(Tipo)

    def __str__(self):
        return self.palavra

