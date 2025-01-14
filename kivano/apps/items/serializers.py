from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name",)


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ("id", "name",)


class SubCategoryListSerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True)
    class Meta:
        model = Category
        fields = ('id','subcategories')


class NestedCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NestedCategory
        fields = ("id", "name",)


class NestedCategoryListSerializer(serializers.ModelSerializer):
    nested_categories = NestedCategorySerializer(many=True)
    class Meta:
        model = SubCategory
        fields = ("id",'nested_categories',)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name','description','price','image')


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ("id", "product", "amount")


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True,)
    class Meta:
        model = Cart
        fields = ("id", "items")


class CartItemAmountSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    image = serializers.ImageField(source="product.image")
    name = serializers.CharField(source="product.name")
    price = serializers.CharField(source="product.price")

    class Meta:
        model = CartItem
        fields = ("id", "product", "image", "name", "price", "amount", "total_price")


class CartItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ("amount",)


