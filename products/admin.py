from django.contrib import admin
from .models import Product, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('parent_id', 'name',)
    list_display_links = ('parent_id', 'name',)
    list_filter = ('parent_id', 'name',)
    search_fields = ('parent_id', 'name',)
    list_per_page = 20

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'price', 'is_published',)
    list_display_links = ('name',)
    list_filter = ('name', 'price',)
    list_editable = ('is_published',)
    search_fields = ('name', 'description',)
    list_per_page = 20

admin.site.register(Product, ProductAdmin)
