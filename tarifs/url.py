from re import I
from django.urls import path
from rest_framework.views import APIView
from . import views
from .views import TarifApi,TarifsEditeApi,TarifsFiltreApi
from rest_framework.authtoken import views


urlpatterns = [
    path('tarifs/', TarifApi.as_view()),
    path('tarifs/<str:id>', TarifsEditeApi.as_view()),
    path('tarifs/filter/', TarifsFiltreApi.as_view()),
]