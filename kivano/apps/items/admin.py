from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') 

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)  


@admin.register(NestedCategory)
class NestedCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',) 


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)  


class CartItemInline(admin.TabularInline):
    model = CartItem
    fields = ["id", "product", "cart", "amount", "total_price",]

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]

