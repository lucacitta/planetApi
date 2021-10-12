from django.core.mail import send_mail

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from apps.planetas.models import PlanetasApi, AdministradorMailApi
from apps.planetas.api.serializers import PlanetasApiSerializer, ContactFormApiSerializer


from planetasApi.settings.base import EMAIL_ADMIN, EMAIL_HOST_USER

@api_view(['GET','POST'])
def planetas_api_view(request):

    if request.method == 'GET':
        planet = PlanetasApi.objects.all()
        planet_serializer = PlanetasApiSerializer(planet, many = True)
        return Response(planet_serializer.data)
    if request.method == 'POST':
        contact_data = ContactFormApiSerializer(data = request.data)
        if contact_data.is_valid():
            print('paso validaciones')
            first_name = contact_data.validated_data.get('first_name')
            last_name = contact_data.validated_data.get('last_name')
            email = contact_data.validated_data.get('email')
            message = contact_data.validated_data.get('message')
            Primero=AdministradorMailApi.objects.all
            # send_mail(
            #     f"Nuevo mensaje de {first_name} en Planet Api",
            #     f'El mensaje es de {first_name} {last_name}, con email {email} y dice lo siguiente: \n{message}',
            #     EMAIL_HOST_USER,
            #     [EMAIL_ADMIN],
            #     fail_silently=False
            # )
            return Response(data = {'message':'El mail se envio correctamente'}, status=status.HTTP_202_ACCEPTED)
        else:
            print('no pasa validaciones')

@api_view(['GET'])
def planetas_api_detail_view(request, pk=None):
    if request.method == 'GET':
        if pk != None:
            planet = PlanetasApi.objects.filter(id = pk).first()
            planet_serializer = PlanetasApiSerializer(planet)
            return Response(planet_serializer.data)


# {
# "first_name":"Luca",
# "last_name":"Citta Giordano",
# "email":"lucacitta@gmail.com",
# "message":"Hola luca querido, porfa podes hacer andar esto? asi ya terminamos, o al menos por ahora"
# }