from rest_framework import serializers
from apps.planetas.models import PlanetasApi

class PlanetasApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanetasApi
        fields = '__all__'

class ContactFormApiSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=10)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    message = serializers.CharField(max_length=350)

