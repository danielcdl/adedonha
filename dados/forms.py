from django.forms import Form
from .models import Tipo
from .models import Palavra


class TipoForm(Form):
    model = Tipo
    fields = '__all__'

class PalavraForm(Form):
    model = Palavra
    fields = '__all__'