from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from .models import Player, NameStatic
from .forms import PlayerForm
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView


def index(request):
    all_player = Player.objects.all()
    all_static = NameStatic.objects.all()
    static_1 = Player.objects.filter(static_id='1')
    static_2 = Player.objects.filter(static_id='2')
    static_3 = Player.objects.filter(static_id='3')
    static_4 = Player.objects.filter(name='На рассмотрении в статик')
    context = {
        'all_player': all_player,
        'title': 'Гильдия Призраки Азерота',
        'all_static': all_static,
        'static_1': static_1,
        'static_2': static_2,
        'static_3': static_3,
        'static_4': static_4,
    }
    return render(request, 'main/index.html', context)


class PlayerCreateView(CreateView):
    template_name = 'main/create.html'
    form_class = PlayerForm
    success_url = reverse_lazy('index')


class PlayerUpdateView(UpdateView):
    model = Player
    fields = '__all__'
    template_name = 'main/update.html'
    def get_object(self):
        pk = self.kwargs['pk']
        player = get_object_or_404(Player, pk=pk)
        return player

    def get_success_url(self):
        return reverse_lazy('index')



