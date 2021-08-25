from django.shortcuts import render

from .models import Wall


def index(request):
    walls = Wall.objects.all()
    context = {
        'walls': walls,
        'title': 'Доска обьявлений'
    }
    return render(request, 'wall/index.html', context)
