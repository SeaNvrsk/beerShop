from django.db import models


class StyleOfBeer(models.Model):
    class Meta:
        verbose_name = 'Тип пива'
        verbose_name_plural = 'Типы пива'

    TYPE_CHOICES = (
        ('ALE', 'Эль'),
        ('LAGER', 'Лагер')
    )

    title = models.CharField(max_length=200, verbose_name="Тип пива")
    typeOfBeer = models.CharField(max_length=10, choices=TYPE_CHOICES, verbose_name="Вид пива")

    def __str__(self):
        return self.title


class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    CONTAINER_CHOICES = (
        ('BOTTLE', 'бутылка'),
        ('PLASTIC', 'пластиковая бутылка'),
        ('CAN', 'банка'),
    )

    name = models.CharField(max_length=200, verbose_name="Название")
    styleOfBeer = models.ForeignKey(StyleOfBeer, on_delete=models.CASCADE, verbose_name="Тип пива")
    container = models.CharField(max_length=20, choices=CONTAINER_CHOICES, verbose_name="Тара")
    size = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Объём")
    image = models.ImageField(upload_to='media/images/product', verbose_name="Изображение", null=True)
    volume = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Крепость")
    beerDensity = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Плотность пива")
    description = models.CharField(max_length=500, verbose_name="Описание")
    manufacturer = models.CharField(max_length=100, verbose_name="Производитель")
    country = models.CharField(max_length=100, verbose_name="Страна")
    inStock = models.BooleanField(default=True)
    price = models.PositiveIntegerField(verbose_name="цена")
    quantity = models.PositiveIntegerField(verbose_name="количество", default=0)

    def __str__(self):
        return self.name


