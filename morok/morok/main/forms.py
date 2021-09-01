from django.forms import ModelForm

from .models import Player


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ('name', 'nick', 'proffesion', 'static_id')



