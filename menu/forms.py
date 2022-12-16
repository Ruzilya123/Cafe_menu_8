
from django import forms
from . import models

choices_noon = [
    ("morning", "Утро"),
    ("day", "День"),
    ("evening", "Вечер"),
]

def get_choices():
    choices = []
    for item in models.Bludo.objects.all():
        choices.append([item.id, item.name])
    return choices

def get_zal_choices():
    choices = []
    for item in models.Zal.objects.all():
        choices.append([item.id, item.name])
    return choices

class ZakazForm(forms.Form):
    fio = forms.CharField(label='ФИО')
    date = forms.DateTimeField(label='Дата торжества')
    noon = forms.ChoiceField(label='Время суток', choices=choices_noon)
    zal = forms.ChoiceField(label='Зал', choices=get_zal_choices())
    bludo1 = forms.ChoiceField(label='Блюдо_1', choices=get_choices())
    bludo3 = forms.ChoiceField(label='Блюдо_3', choices=get_choices())
    bludo2 = forms.ChoiceField(label='Блюдо_2', choices=get_choices())
    peoples = forms.IntegerField(label='Количество человек')
    agree = forms.BooleanField(label='Согласие на обработку данных')

