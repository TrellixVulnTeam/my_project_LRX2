from django.db import models


class Wall(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название товара')
    content = models.TextField(max_length=500, null=True, blank=True, verbose_name='Описание')

    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')

    class Meta:
        verbose_name_plural = 'Обьявления'
        verbose_name = 'Обьявление'
        ordering = ['-published']

