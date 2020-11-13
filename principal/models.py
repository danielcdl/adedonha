from django.contrib.auth import get_user_model
from django.db.models import CASCADE
from django.db.models import CharField
from django.db.models import EmailField
from django.db.models import ForeignKey
from django.db.models import Model


class Jogador(Model):
    user = ForeignKey(get_user_model(), on_delete=CASCADE)
    nome = CharField(unique=True, max_length=100)
    email = EmailField(unique=True)

    def __str__(self):
        return self.nome
