from django.db import models
from core.models import DomesticProduct,AddDomesticItem

class DomesticProducts(DomesticProduct):
    class Meta:
        verbose_name = 'Domestic Product'
        verbose_name_plural = 'Domestic Products'
        proxy = True


class DomesticItems(AddDomesticItem):
    class Meta:
        proxy = True
        verbose_name = 'Domestic Product Item'
        verbose_name_plural = 'Domestic Products Items'