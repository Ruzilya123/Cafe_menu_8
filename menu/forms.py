
from django import forms
from . import models

choices_time = [
    ("morning", "Утро"),
    ("day", "День"),
    ("evening", "Вечер"),
]

choices = []
for item in models.Bludo.objects.all():
    choices.append([item.name, item.name])

class ZakazForm(forms.Form):
    fio = forms.CharField(label='ФИО')
    date = forms.DateTimeField(label='Дата торжества')
    time = forms.ChoiceField(label='Время суток', choices=choices_time)
    bludo1 = forms.ChoiceField(label='Блюдо_1', choices=choices)
    bludo2 = forms.ChoiceField(label='Блюдо_2', choices=choices)
    bludo3 = forms.ChoiceField(label='Блюдо_3', choices=choices)
    peoples = forms.IntegerField(label='Количество человек')
    agreement = forms.BooleanField(label='Согласие на обработку данных')

