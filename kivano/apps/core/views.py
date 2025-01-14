from django.shortcuts import render
from rest_framework import generics, mixins, viewsets
from .models import *
from .serializers import *

class AdvertisingViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Advertising.objects.all()
    serializer_class = AdvertisingSerializer


class PlatformLinkViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = PlatformLink.objects.all()
    serializer_class = PlatformLinkSerializer

class ContactViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer