import re
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from apps.planetas.models import PlanetasApi
from apps.planetas.api.serializers import PlanetasApiSerializer


@api_view(['GET','POST'])
def planetas_api_view(request):

    if request.method == 'GET':
        planet = PlanetasApi.objects.all()
        planet_serializer = PlanetasApiSerializer(planet, many = True)
        return Response(planet_serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def planetas_api_detail_view(request, pk=None):
    if request.method == 'GET':
        if pk != None:
            planet = PlanetasApi.objects.filter(id = pk).first()
            if planet:
                planet_serializer = PlanetasApiSerializer(planet)
                return Response(planet_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'message':'Error, no se encuentra el planeta'})
