#from tkinter.tix import Tree
from unittest import result
from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from rest_framework.relations import method_overridden
from .models import Tarifs


class getIdRepresentation(serializers.RelatedField):
    def to_representation(self, value):
        result = {}
        #result['_id']= value.id
        return result 

class TarifSerializer(serializers.ModelSerializer):
    #commentaire = getIdRepresentation(read_only=True,many=False)
    class Meta:
        model= Tarifs
        fields = '__all__'

