from django.forms import ModelForm

from .models import Wall


class WallForm(ModelForm):
    class Meta:
        model = Wall
        fields = ('title', 'content', 'price', 'rubric')
