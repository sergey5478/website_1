from django.db import models


class Trubi(models.Model):
    name = models.CharField('Тип/название трубы', max_length=100)
    wall = models.CharField('Cтенка (мм)', max_length=10)
    length = models.CharField('Длина (Метры)', max_length=10)
    weight = models.CharField('Вес 1 единицы (в погонных метрах)', max_length=10)
    price = models.CharField('Цена 1 единицы (в погонных метрах)', max_length=10)
    priceT = models.CharField('Цена 1 Тонны (в погонных метрах)', max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'трубу в таблицу "Трубы"'


class Image(models.Model):
    image = models.ImageField(upload_to='media/hellodj/')
