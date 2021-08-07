from rest_framework import fields, serializers
from .models import Datamodel

class DatamodelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datamodel
        fields ='__all__'