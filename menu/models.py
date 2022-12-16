from django.db import models

class Zal(models.Model):
    name = models.CharField('name', 'name', max_length=24)

class Bludo(models.Model):
    name = models.CharField('name', 'name', max_length=24)

class Zakaz(models.Model):
    fio = models.CharField('fio', 'fio', max_length=24)
    date = models.DateField('date', 'date')
    noon = models.CharField('noon', 'noon', max_length=10)
    peoples = models.IntegerField('peoples', 'peoples')
    agree = models.BooleanField('agree', 'agree', null=False, default=True)
    zal = models.ForeignKey(Zal, on_delete=models.CASCADE)
    bludo = models.ManyToManyField(Bludo)

