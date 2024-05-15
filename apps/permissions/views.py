from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Permissions, UserPermissions
from .serializers import PermissionsSerializer, UserPermissionsSerializer


class PermissionList(APIView):
    """
    List all permissions, or create a new permission
    """

    def get(self, request, format=None):
        permissions = Permissions.objects.all()
        serializer = PermissionsSerializer(permissions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PermissionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PermissionDetail(APIView):
    """
    Retrieve, update or delete a permission instance
    """

    def get_object(self, pk):
        try:
            return Permissions.objects.get(pk=pk)
        except Permissions.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        permission = self.get_object(pk)
        serializer = PermissionsSerializer(permission)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        permission = self.get_object(pk)
        serializer = PermissionsSerializer(permission, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        permission = self.get_object(pk)
        permission.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserPermissionList(APIView):
    """
    List all permissions for a user
    """

    def get(self, request, format=None):
        user_permissions = UserPermissions.objects.all()
        serializer = UserPermissionsSerializer(user_permissions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserPermissionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
