from django.shortcuts import render
from jsonschema import ValidationError
from rest_framework import generics,mixins,viewsets,status
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import serializers
from .models import *

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions


class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = SubCategoryListSerializer


class NestedCategoryViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = NestedCategoryListSerializer


class ProductViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        user = request.user
        items = request.data.get("items", [])

        cart, _ = Cart.objects.get_or_create(user=user)
        for item in items:
            product_id = item.get("product")
            amount = item.get("amount", 1)

            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return Response({"error": f"Продукт с ID {product_id} не найден"}, status=400)

            cart_item, _ = CartItem.objects.get_or_create(cart=cart, product=product)
            cart_item.amount += amountЕ
            cart_item.save(update_fields=["amount"])

        return Response(CartSerializer(cart).data)


class CartItemViewSet(mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    authentication_classes = [JWTAuthentication,]

    def destroy(self, request, *args, **kwargs):
        user = request.user

        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            return Response({"error": "Корзина пользователя не найдена"}, status=status.HTTP_404_NOT_FOUND)

        product_id = kwargs.get("pk")

        if not product_id:
            return Response({"error": "Поле product не указано в URL"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            cart_item = CartItem.objects.get(cart=cart, product_id=product_id)
            cart_item.delete()
            return Response({"success": "Товар был удален из корзины"}, status=status.HTTP_200_OK)
        except CartItem.DoesNotExist:
            return Response({"error": "Товар не найден в корзине"}, status=status.HTTP_404_NOT_FOUND)


class CardItemListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CartItemAmountSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return CartItem.objects.filter(cart__user=user)


class CartItemUpdateViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemUpdateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        cart = self.request.user.cart
        return CartItem.objects.filter(cart__user=user, cart=cart)


class CartTotalPriceViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Cart.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        cart = request.user.cart

        total_price = 0
        for item in cart.items.all():
            total_price += item.total_price

        return Response({"total_price": total_price})