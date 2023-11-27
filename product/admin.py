from django.contrib import admin

from product.models import Product, Category


# Register your models here.
# admin.site.register(Student)

@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'price', 'category', 'date_create', 'date_change', 'picture')
    list_filter = ('category',)
    search_fields = ('name', 'description')

