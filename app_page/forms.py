from django.forms import ModelForm
from .models import Cars


class CarsModel(ModelForm):
    class Meta:
        model = Cars
        fields = "__all__"