from rest_framework import routers
from .views import *

core_router = routers.DefaultRouter()

core_router.register(r"advertising", AdvertisingViewSet, basename="advertising")
core_router.register(r"networks", PlatformLinkViewSet, basename="networks")
core_router.register(r"contact", ContactViewSet, basename="contact")