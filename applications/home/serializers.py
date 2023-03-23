
#DJANGO REST-FRAMEWORK
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView


#models
from .models import DatosHome

class DatosHomeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DatosHome
        fields = ("contador_clicks_wthasapp",)