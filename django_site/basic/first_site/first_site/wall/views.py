from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Wall
from .models import Rubric
from .forms import WallForm


def index(request):
    walls = Wall.objects.all()
    rubrics = Rubric.objects.all()
    context = {
        'walls': walls,
        'title': 'Доска обьявлений',
        'rubrics': rubrics
    }
    return render(request, 'wall/index.html', context)


def by_rubric(request, rubric_id):
    walls = Wall.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {
        'walls': walls,
        'rubrics': rubrics,
        'current_rubric': current_rubric
    }
    return render(request, 'wall/by_rubric.html', context)


class WallCreateView(CreateView):
    template_name = 'wall/create.html'
    form_class = WallForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context