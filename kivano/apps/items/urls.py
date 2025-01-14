from rest_framework import routers
from .views import *

items_router = routers.DefaultRouter()

items_router.register(r"category_list", CategoryViewSet, basename="category_list")
items_router.register(r"sub_category_item", SubCategoryViewSet, basename="sub_category_item")
items_router.register(r"nested_category_item", NestedCategoryViewSet, basename="nested_category_item")
items_router.register(r"products", ProductViewSet, basename="products")
items_router.register(r"cart_list", CardItemListViewSet, basename="cart_list")
items_router.register(r"cart_item_update", CartItemUpdateViewSet, basename="cart_item_update")
items_router.register(r"cart_total_price", CartTotalPriceViewSet, basename="cart_total_price")
items_router.register(r"cart", CartViewSet, basename="cart")