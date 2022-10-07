
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres import fields as PostgreFields

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(max_length=256)
    icon_url = models.URLField(blank=True)
    description = models.TextField()
    parent_category = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        related_name="children_categories",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class Maker(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    
    class Currency(models.TextChoices):
        INDIAN_RUPEE = ("INR", _("Indian Rupee"))
        AMERICAN_DOLLER = ("USD",("American Doller"))
        YEN = ("JPY",_("Japan Yen"))
        EURO =("EUR",_("Euro"))
        
    title = models.CharField(max_length=512)
    subtitle = models.CharField(max_length=512)
    maker = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name="products",
        blank=True,
        null=True,
    )
    image1_url = models.URLField(blank=True , null=True)
    image2_url = models.URLField(blank=True , null=True)
    image3_url = models.URLField(blank=True , null=True)
    image4_url = models.URLField(blank=True , null=True)
    
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    
    currency = models.CharField(
        max_length = 3,
        choices = Currency.choices,
        default = Currency.AMERICAN_DOLLER,
    )
    
    variation_product_ids = PostgreFields.ArrayField(
        models.IntegerField(null=True,blank=True),
        null=True,
        blank=True,
    )
    
    def __str__(self) -> str:
        return f"{self.title} - {self.subtitle} - {self.maker}"