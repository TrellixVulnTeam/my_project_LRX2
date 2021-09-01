from django.db import models


class NameStatic(models.Model):
    name = models.CharField(max_length=50, null=True, verbose_name='Название статика')

    class Meta:
        verbose_name = 'Статик'
        verbose_name_plural = 'Статики'
        ordering = ['-name']

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=50, null=True, verbose_name='Имя')
    nick = models.CharField(max_length=50, null=False, verbose_name='Ник в игре')
    proffesion = models.CharField(max_length=50, null=True, verbose_name='Спек')
    static_id = models.ForeignKey('NameStatic', null=True,
                                  blank=True,
                                  on_delete=models.PROTECT,
                                  verbose_name='Название статика')

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'
        ordering = ['name']
