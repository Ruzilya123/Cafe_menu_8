from django.shortcuts import render
from .forms import ZakazForm
from rest_framework.views import APIView
from . import models, forms
from .serializers import ZakazSerializer, BludoSerializer, ZalSerializer
from rest_framework.response import Response

def index(request):
    zakazform = ZakazForm()
    return render(request, "index.html", {"form":zakazform})

class ZalList(APIView):
    def get(self, request, format=None):
        snippets = models.Zal.objects.all()
        serializer = ZalSerializer(snippets, many=True)
        return Response(serializer.data)

class BludoList(APIView):
    def get(self, request, format=None):
        snippets = models.Bludo.objects.all()
        serializer = BludoSerializer(snippets, many=True)
        return Response(serializer.data)

class ZakazList(APIView):
    def get(self, request, format=None):
        snippets = models.Zakaz.objects.all()
        serializer = ZakazSerializer(snippets, many=True)
        return Response(serializer.data)