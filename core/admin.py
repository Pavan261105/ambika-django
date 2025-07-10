from django.contrib import admin
from .models import Category, Product, ProductImage
# templatetags/extras.py
from django import template

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock')
    inlines = [ProductImageInline]

admin.site.register(Category)


register = template.Library()

@register.filter
def make_chunks(value, chunk_size):
    chunk_size = int(chunk_size)
    return [value[i:i + chunk_size] for i in range(0, len(value), chunk_size)]
