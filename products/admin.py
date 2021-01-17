from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'price', 'is_published',)
    list_display_links = ('name',)
    list_filter = ('name', 'price',)
    list_editable = ('is_published',)
    search_fields = ('name', 'description',)
    list_per_page = 20

admin.site.register(Product, ProductAdmin)
