from django.contrib import admin
from .models import *
from admin_auto_filters.filters import AutocompleteFilter
from django.utils.html import format_html
from rangefilter.filter import DateRangeFilter
from search_admin_autocomplete.admin import SearchAutoCompleteAdmin

from import_export.admin import ImportExportModelAdmin
from django.forms import TextInput
from jet.filters import DateRangeFilter


class MyModelAdmin(SearchAutoCompleteAdmin):
    ''' Search field on admin'''
    search_fields = ["search_field",]

class CatagoryFilter(AutocompleteFilter):
    ''' Autofield on Category '''
    title = 'Category' # display title
    field_name = 'category' # name of the foreign key field

class SubCatagoryFilter(AutocompleteFilter):
    ''' Autofield on Subcategory '''
    
    title = 'Subcatagory' # display title
    field_name = 'subcatagory'

'''
DOMESTIC
'''
class ProductInline(admin.TabularInline):
    model = AddDomesticItem
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
    


'''
FILTER's
'''
@admin.register(ProductOption)
class ProductOptionAdmin(admin.ModelAdmin):
    list_per_page = 6
    search_fields = ("sku","optionname",)
    list_display = ["optionname","optionvalue","sku","markuprate"]

@admin.register(AdditionalOption)
class AdditionalOptionAdmin(admin.ModelAdmin):
    list_per_page = 6
    search_fields = ("sku","optionname",)
    list_display = ["optionname","optionvalue","sku","markuprate"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_per_page = 6
    search_fields = ("category",)
    list_filter = ("category","region")
    list_display = ["category","region"]

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_per_page = 6
    search_fields = ("subcategory",)
    list_filter = ("region","category",)
    list_display = ["subcategory","category","region"]

@admin.register(SubSubCategory)
class SubSubCategoryAdmin(admin.ModelAdmin):
    list_per_page = 6
    search_fields = ("subsubcategory",)
    list_filter = ("region","category","subcategory",)
    list_display = ["subsubcategory","subcategory","category","region"]


'''
For all Iteams import export functionality
'''




admin.site.register(Region)

admin.site.site_header = "Admin Dashboard"
admin.site.site_title = "Admin Dashboard"
admin.site.index_title = "Welcome to Admin Dashboard"