from rest_framework import serializers
from apps.planetas.models import PlanetasApi

class PlanetasApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanetasApi
        fields = '__all__'
