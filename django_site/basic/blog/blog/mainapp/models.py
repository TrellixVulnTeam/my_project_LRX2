from django.db import models


class Article(models.Model):
    image = models.ImageField(verbose_name="Изображение", upload_to='article/')
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    text = models.TextField(verbose_name='Текст')
    description = models.TextField(verbose_name='Описание', max_length=300)
    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateField(verbose_name='Дата обновления', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
