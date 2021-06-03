from django.contrib import admin
from .models import DomesticProductSize,DomesticSizeItem
from .models import *
from django.utils.html import format_html

from import_export.admin import ImportExportModelAdmin
from django.forms import TextInput
from jet.filters import DateRangeFilter

class ProductInlineSize(admin.TabularInline):
    model = DomesticSizeItem
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.IntegerField: {'widget': TextInput(attrs={'size':'10'})},
        models.FloatField: {'widget': TextInput(attrs={'size':'10'})},
        # models.ForeignKey: {'widget': TextInput(attrs={'size':'10'})}
    }

@admin.register(DomesticProductSize)
class ProductAdminSize(ImportExportModelAdmin,admin.ModelAdmin):
    def delete (self, obj):
        return format_html('<input type="button" style="background-color:#ba2121;" value="Delete" onclick="location.href=\'{0}/delete/\'" />'.format(obj.pk))

    delete.allow_tags = True
    delete.short_description ='Delete Product'
    list_per_page = 6
    fieldsets = (
        (None, {
           'fields': ( ("sku","productname"),("region","category","subcatagory","subsubcategory"),
            ("markup","productcostc","targetgrossprofit")
       )     
    }),
    )
    search_fields = ("sku","productname")
    list_filter = ("sku","productname","category","subcatagory",
    ('created_at', DateRangeFilter),
    ('updated_at', DateRangeFilter))
    list_display = ("sku","productname","category","subcatagory",'delete')
    inlines = [
        ProductInlineSize,
    ]

@admin.register(DomesticSizeItem)
class DomesticSizeItemAdmin(ImportExportModelAdmin):
     list_per_page = 6
     list_display = ["product","quantity"]
     list_filter = ("product",)