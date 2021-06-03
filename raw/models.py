from django.db import models
from core.models import DomesticProductRaw,AddDomesticRawItem
# Create your models here.

class DomesticRawProduct(DomesticProductRaw):
    class Meta:
        verbose_name = 'Domestic Raw Product'
        verbose_name_plural = 'Domestic Raw Products'
        proxy = True


class DomesticRawItems(AddDomesticRawItem):
    class Meta:
        proxy = True
        verbose_name = 'Domestic Raw Product Item'
        verbose_name_plural = 'Domestic Raw Products Items'
    