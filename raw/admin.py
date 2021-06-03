from django.contrib import admin
from core.models import AddDomesticRawItem
from django.contrib import admin
from .models import *
from django.utils.html import format_html
from import_export.admin import ImportExportModelAdmin
from django.forms import TextInput
from jet.filters import DateRangeFilter

class ProductInlineDomesticRaw(admin.TabularInline):
    model = DomesticRawItems
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size':'10'})},
        models.FloatField: {'widget': TextInput(attrs={'size':'8'})},
        # models.ForeignKey: {'widget': TextInput(attrs={'size':'10'})}
    }
    extra = 1

class ProductAdminDomesticRaw(ImportExportModelAdmin,admin.ModelAdmin):
    def delete (self, obj):
        return format_html('<input type="button" style="background-color:#ba2121;" value="Delete" onclick="location.href=\'{0}/delete/\'" />'.format(obj.pk))

    delete.allow_tags = True
    delete.short_description ='Delete Product'
    list_per_page = 10
    search_fields = ("sku","productname",)
    fieldsets = (
        (None, {
        'fields': (
        ("sku","productname"),("region","category","subcatagory","subsubcategory"))
        }),
        ('Additives', {
            'classes': ('collapse', 'open'),
            'fields': (("firstcost","printval","transfer","packing"),
            ("markup","duty","exchage","broker"),
            ("sewing","fleece","printedoutside","overhead"),
            ("freight"))
        }),  
        )
    list_filter = ("sku","productname","category","subcatagory",
    ('created_at', DateRangeFilter),
    ('updated_at', DateRangeFilter))
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size':'10'})},
        models.FloatField: {'widget': TextInput(attrs={'size':'10'})},
    }
    list_display = ("sku","productname","category","subcatagory",'delete')
    inlines = [
        ProductInlineDomesticRaw,
    ]

@admin.register(DomesticRawItems)
class AddDomesticRawItemAdmin(ImportExportModelAdmin):
     list_per_page = 6
     search_fields = ("product",)
     list_filter = ("product",)
     list_display = ["product","quantity","marketval","price"]

admin.site.register(DomesticRawProduct,ProductAdminDomesticRaw)

