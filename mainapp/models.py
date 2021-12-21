from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(
        verbose_name='имя',
        max_length=64,
        unique=True
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        )
    name = models.CharField(
        verbose_name='имя продукта',
        max_length=130,
        )
    image = models.ImageField(
        upload_to='продукт_images',
        blank=True,
        )
    shot_desc = models.CharField(
        verbose_name='краткое описание продукта',
        max_length=70,
        blank=True,
        )
    description = models.TextField(
        verbose_name='описание продукта',
        blank=True,
        )
    price = models.DecimalField(
        verbose_name='цена продукта',
        max_digits=8,
        decimal_places=2,
        default=0,
        )
    quantity = models.PositiveIntegerField(
        verbose_name='количество на складе',
        default=0,
    )


    def  __str__(self):
        return f"{self.name} ({self.category.name})"

