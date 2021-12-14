from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article


class MainListView(ListView):
    """ Вывод главной страницы со всеми статьями """
    model = Article
    queryset = Article.objects.all()
    template_name = 'mainapp/index.html'
    context_object_name = 'articles'


class ArticleDetailView(DetailView):
    """ Вывод полного описания статьи """
    model = Article
    template_name = 'mainapp/article_detail.html'
    context_object_name = 'article'
