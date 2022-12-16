
from rest_framework import serializers
from . import models

class ZalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Zal
        fields = ['name']

class BludoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bludo
        fields = ['name']

class ZakazSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Zakaz
        fields = ['fio', 'date', 'noon', 'peoples', 'agreement', 'zal', 'bludo']

