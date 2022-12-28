from django.contrib import admin
from .models import Category, Color, Product, ProductFeature, ProductImage

# Register your models here.


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductFeatureInline(admin.TabularInline):
    model = ProductFeature


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ProductFeatureInline]


admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Product, ProductAdmin)
