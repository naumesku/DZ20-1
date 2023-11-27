from django.db import models

# Create your models here.

NULLABLE = {'blank': True, 'null': True}

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    picture = models.ImageField(upload_to='product/', verbose_name='изображение', **NULLABLE)
    category = models.CharField(max_length=200, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за покупку')
    date_create = models.DateTimeField(verbose_name='дата создания')
    date_change = models.DateTimeField(verbose_name='дата последнего изменения')


    def __str__(self):
        return f'{self.name} {self.description} {self.picture} {self.category} {self.price} {self.date_create} {self.date_change}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'