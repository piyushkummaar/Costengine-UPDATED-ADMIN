from django.db import models
from core.models import ImportsProduct,AddImportsItem
# Create your models here.

class ImportsProducts(ImportsProduct):
    class Meta:
        verbose_name = 'Imports Product'
        verbose_name_plural = 'Imports Products'
        proxy = True


class ImportsItem(AddImportsItem):
    class Meta:
        proxy = True
        verbose_name = 'Imports Product Item'
        verbose_name_plural = 'Imports Products Items'