
from django.urls import path
from . import views

urlpatterns = [
    path('zals/', views.ZalList.as_view()),
    path('bludos/', views.BludoList.as_view()),
    path('zakaz/', views.ZakazList.as_view()),
    path('', views.index)
]
