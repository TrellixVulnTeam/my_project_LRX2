from django.db import models


class Rubric(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
        ordering = ['name']

    def __str__(self):
        return self.name

class Wall(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название товара')
    content = models.TextField(max_length=500, null=True, blank=True, verbose_name='Описание')

    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')

    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = 'Обьявления'
        verbose_name = 'Обьявление'
        ordering = ['-published']


