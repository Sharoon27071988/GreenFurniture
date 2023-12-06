from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name[:30]

    def get_absolute_url(self):
        return reverse('category', kwargs={'pk': self.pk})


class Type(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='types',
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'Вид'
        verbose_name_plural = 'Виды'

    def __str__(self):
        return self.name[:30]


class Manufacturer(models.Model):
    description = models.TextField(verbose_name='Описание')
    name = models.CharField(max_length=200, verbose_name='Название')

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.name[:30]


class Furniture(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='furniture/', verbose_name='Картинка')
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name='furniture',
        verbose_name='Производитель'
    )
    type = models.ForeignKey(
        Type,
        on_delete=models.SET_NULL,
        null=True,
        related_name='furniture',
        verbose_name='Вид'
    )

    class Meta:
        verbose_name = 'Мебель'
        verbose_name_plural = 'Мебель'

    def __str__(self):
        return self.name[:30]

    def get_absolute_url(self):
        return reverse('furniture_detail', kwargs={'pk': self.pk})
