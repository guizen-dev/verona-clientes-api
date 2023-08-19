from .models import Cliente
from .serializers import ClienteSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from django.http.response import JsonResponse


@api_view(['GET', 'POST', 'DELETE'])
def all_clientes(request):
    if request.method == 'GET':
        cliente = Cliente.objects.all()
        cliente_serializer = ClienteSerializer(cliente, many=True)
        return JsonResponse(cliente_serializer.data, safe=False)
    
    
    elif request.method == 'POST':
        cliente_serializer = ClienteSerializer(data=request.data)
        if cliente_serializer.is_valid():
            cliente_serializer.save()
            return JsonResponse(cliente_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(cliente_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cliente = Cliente.objects.all()
        cliente.delete()
        return JsonResponse({'message' : 'Clientees deletados com sucesso!'}, status=status.HTTP_204_NO_CONTENT)