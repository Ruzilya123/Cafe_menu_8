from django.shortcuts import render
from .forms import ZakazForm
from rest_framework.views import APIView
from . import models, forms
from .serializers import ZakazSerializer, BludoSerializer, ZalSerializer
from rest_framework.response import Response
from .models import Zakaz, Zal, Bludo

def index(request):
    zakazform = ZakazForm()

    if request.method == "POST":
        zakazform = ZakazForm(request.POST)

        if not zakazform.is_valid():
            return render(request, "index.html", {"form":zakazform})

        fio = zakazform.cleaned_data['fio']
        date = zakazform.cleaned_data['date']
        noon = zakazform.cleaned_data['noon']
        peoples = zakazform.cleaned_data['peoples']
        agree = zakazform.cleaned_data['agree']
        zal = zakazform.cleaned_data['zal']
        zal_model = Zal.objects.get(pk=zal) 
        bludo1 = Bludo.objects.get(pk=zakazform.cleaned_data['bludo1'])
        bludo2 = Bludo.objects.get(pk=zakazform.cleaned_data['bludo2'])
        bludo3 = Bludo.objects.get(pk=zakazform.cleaned_data['bludo3'])
        zakaz = Zakaz(fio=fio, date=date, noon=noon, zal=zal_model, peoples=peoples, agree=agree)
        zakaz.save()
        zakaz.bludo.add(bludo1, bludo2, bludo3)
        zakaz.save()
        return render(request, "index.html", {"form":zakazform})

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