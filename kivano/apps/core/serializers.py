from rest_framework import serializers
from .models import *

class AdvertisingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertising
        fields = '__all__'

class PlatformLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformLink
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'