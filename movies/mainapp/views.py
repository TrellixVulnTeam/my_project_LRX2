from django.shortcuts import render
from django.views.generic.base import View
from .models import Movie


class MoviesView(View):

    def get(self, request):
        queryset = Movie.objects.all()
        return render(request, 'mainapp/index.html', {'movies': queryset})
