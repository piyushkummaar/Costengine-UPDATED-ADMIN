from django.db import models
from core.models import DomesticSizeProduct,AddDomesticSizeItem
# Create your models here.

class DomesticProductSize(DomesticSizeProduct):
    class Meta:
        verbose_name = 'Domestic Size Product'
        verbose_name_plural = 'Domestic Size Products'
        proxy = True


class DomesticSizeItem(AddDomesticSizeItem):
    class Meta:
        proxy = True
        verbose_name = 'Domestic Size Product Item'
        verbose_name_plural = 'Domestic Size Products Items'