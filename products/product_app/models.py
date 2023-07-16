from django.db import models

# Create your models here.
class Product(models.Model):
    UNITS = (
        (1, 'шт.'),
        (2, 'кг.'),
    )

    name = models.CharField(verbose_name='Наименование', max_length=128)
    date = models.DateField(verbose_name='дата поступления')
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=0, default=0)
    unit = models.IntegerField(verbose_name='единица измерения', choices=UNITS)
    provider = models.CharField(verbose_name='Поставщик', max_length=256, blank=True)

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
