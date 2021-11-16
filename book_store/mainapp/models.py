from django.db import models


class BookCategory(models.Model):
    """"Класс-модель Категория книг"""
    title = models.CharField(max_length=64, blank=False, verbose_name='Название категории')
    short_description = models.CharField(max_length=128, blank=True, verbose_name='Краткое описание')

    class Meta:
        verbose_name = 'Категория книг'
        verbose_name_plural = 'Категории книг'

    def __str__(self):
        return self.title


class Book(models.Model):
    """"Класс-модель Книга """
    category = models.ForeignKey(BookCategory, default=0, on_delete=models.SET_DEFAULT, verbose_name='Категория')
    title = models.CharField(max_length=64, blank=False, verbose_name='Название книги')
    short_description = models.CharField(max_length=128, blank=True, verbose_name='Краткое описание')
    description = models.TextField(blank=True, verbose_name='Подробное описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='Цена')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'{self.title} {self.category.title}'


class Author(models.Model):
    """Класс-модель Автор """
    name = models.CharField(max_length=64, verbose_name='Имя')
    last_name = models.CharField(max_length=64, verbose_name='Фамилия')
    birthday = models.DateField(verbose_name='Дата рождения')
    description = models.TextField(blank=True, verbose_name='О авторе')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return f'{self.name} {self.last_name}'
