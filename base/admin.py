from django.contrib import admin
from .models import *
from admin_auto_filters.filters import AutocompleteFilter
from django.utils.html import format_html
from rangefilter.filter import DateRangeFilter
from search_admin_autocomplete.admin import SearchAutoCompleteAdmin

from import_export.admin import ImportExportModelAdmin
from django.forms import TextInput
from jet.filters import DateRangeFilter

class ProductInline(admin.TabularInline):
    model = DomesticItems
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.IntegerField: {'widget': TextInput(attrs={'size':'10'})},
        models.FloatField: {'widget': TextInput(attrs={'size':'10'})},
        # models.ForeignKey: {'widget': TextInput(attrs={'size':'10'})}
    }

class ProductAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    def delete (self, obj):
        return format_html('<input type="button" style="background-color:#ba2121;" value="Delete" onclick="location.href=\'{0}/delete/\'" />'.format(obj.pk))

    delete.allow_tags = True
    delete.short_description ='Delete Product'
    list_per_page = 6
    search_fields = ("sku","productname")
    fieldsets = (
        (None, {
           'fields': ( ("sku","productname"),("region","category","subcatagory","subsubcategory"),
            ("markup","productcostc","targetgrossprofit")
       )     
    }),
    )
    # list_filter = (CatagoryFilter,SubCatagoryFilter,
    #     ('created_at', DateRangeFilter), ('updated_at', DateTimeRangeFilter),
    # )
    list_filter = ("sku","productname","category","subcatagory",
    ('created_at', DateRangeFilter),
    ('updated_at', DateRangeFilter))
    list_display = ("sku","productname","category","subcatagory",'delete')
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size':'10'})},
        models.FloatField: {'widget': TextInput(attrs={'size':'10'})},
        }
    inlines = [
        ProductInline,
    ]

@admin.register(DomesticItems)
class AddDomesticItemAdmin(ImportExportModelAdmin):
     list_per_page =  6
     list_display = ["product","quantity","price"]
     list_filter = ("product",)
admin.site.register(DomesticProducts,ProductAdmin)