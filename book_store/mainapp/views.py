from django.shortcuts import render
from .models import Book, BookCategory,Author
from django.views.generic.list import ListView


class IndexListView(ListView):
    model = Book
    template_name = 'mainapp/index.html'
    context_object_name = 'books'
    # book_category = BookCategory.objects.all()
    # extra_context = {'book_category': book_category}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        book_category = BookCategory.objects.all()
        context['book_category'] = book_category
        context['cat_selected'] = 0
        return context


class ContactsListView(ListView):
    model = Book
    template_name = 'mainapp/contacts.html'

class AuthorListView(ListView):
    model = Author
    template_name = 'mainapp/author.html'
    context_object_name = 'authors'

