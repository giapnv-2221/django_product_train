from django.contrib import admin, sites
from . import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'info', 'price', 'created_at']
    list_filter = ['updated_at']
    search_fields = ['name', 'price']


class ProductInline(admin.StackedInline):
    model = models.Products


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    inlines = [ProductInline]


admin.site.register(models.Products, ProductAdmin)
admin.site.register(models.Categories, CategoryAdmin)
