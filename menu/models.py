from django.db import models

class Zal(models.Model):
    name = models.CharField('name', 'name', max_length=24)

class Bludo(models.Model):
    name = models.CharField('name', 'name', max_length=24)

class Zakaz(models.Model):
    fio = models.CharField('fio', 'fio', max_length=24)
    date = models.DateTimeField('date', 'date')
    time = models.CharField('time', 'time', max_length=10)
    peoples = models.IntegerField('peoples', 'peoples')
    agreement = models.BooleanField('agreement', 'agreement')
    zal = models.ForeignKey(Zal, on_delete=models.CASCADE)
    bludo = models.ManyToManyField(Bludo)

