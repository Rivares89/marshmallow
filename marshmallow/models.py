from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Marshmallow(models.Model):
    name =models.CharField(max_length=100, verbose_name='название')
    description = models.CharField(max_length=100, verbose_name='описание')
    image = models.ImageField(upload_to='marshmallow/',
                              verbose_name='изображение', **NULLABLE)
    price = models.IntegerField(verbose_name='цена')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.SET_NULL,
                              **NULLABLE, verbose_name='владелец')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'зефир'
        verbose_name_plural = 'зефиры'
