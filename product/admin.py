from django.contrib import admin

from product.models import Product, Category, Version


# Register your models here.
# admin.site.register(Student)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'price', 'category', 'date_create', 'date_change', 'picture')
    list_filter = ('category',)
    search_fields = ('name', 'description')

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'version_number', 'version_title', 'is_relevant')
    list_filter = ('product',)
    search_fields = ('name', 'is_relevant',)
