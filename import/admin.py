from django.contrib import admin
from .models import ImportsProducts,ImportsItem
from jet.filters import DateRangeFilter
from import_export.admin import ImportExportModelAdmin

class ProductInlineImports(admin.TabularInline):
    model = ImportsItem
    
class ProductAdminImports(ImportExportModelAdmin,admin.ModelAdmin):
    def delete (self, obj):
        return format_html('<input type="button" style="background-color:#ba2121;" value="Delete" onclick="location.href=\'{0}/delete/\'" />'.format(obj.pk))

    delete.allow_tags = True
    delete.short_description ='Delete Product'
    list_per_page = 10
    search_fields = ("sku","productname",)
    list_filter = ("sku","productname","category","subcatagory",
    ('created_at', DateRangeFilter),
    ('updated_at', DateRangeFilter))
    list_display = ("sku","productname","category","subcatagory",'delete')
    inlines = [
        ProductInlineImports,
    ] 

@admin.register(ImportsItem)
class AddImportsItemAdmin(ImportExportModelAdmin):
     list_per_page = 6
     list_display = ["product","quantity","price"]
     list_filter = ("product",)

admin.site.register(ImportsProducts,ProductAdminImports)