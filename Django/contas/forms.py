from django.forms import ModelForm
from .models import Transation

class TransationForm(ModelForm):
    class Meta:
        model = Transation
        fields = ['date', 'describe', 'value', 'category', 'observations']