from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from .models import Article
from .forms import ArticleForm


class MainListView(ListView):
    """ Вывод главной страницы со всеми статьями """
    model = Article
    queryset = Article.objects.all()
    template_name = 'mainapp/index.html'
    context_object_name = 'articles'
    extra_context = {'title': 'Blog'}


class ArticleDetailView(DetailView):
    """ Вывод полного описания статьи """
    model = Article
    template_name = 'mainapp/article_detail.html'
    context_object_name = 'article'
    extra_context = {'title': 'Blog'}


class ArticleCreateView(CreateView):
    template_name = 'mainapp/add_article.html'
    form_class = ArticleForm
    success_url = reverse_lazy('main')
