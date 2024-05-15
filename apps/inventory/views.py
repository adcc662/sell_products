from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Inventory
from .serializers import InventorySerializer


class InventoryList(APIView):
    def get(self, request):
        inventory = Inventory.objects.all()
        serializer = InventorySerializer(inventory, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InventoryDetail(APIView):
    def get_object(self, pk):
        try:
            return Inventory.objects.get(pk=pk)
        except Inventory.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        inventory = self.get_object(pk)
        serializer = InventorySerializer(inventory)
        return Response(serializer.data)

    def put(self, request, pk):
        inventory = self.get_object(pk)
        serializer = InventorySerializer(inventory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        inventory = self.get_object(pk)
        inventory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
