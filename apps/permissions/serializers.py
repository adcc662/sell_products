from rest_framework import serializers
from .models import Permissions, UserPermissions


class PermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissions
        fields = ['id', 'name', 'description']


class UserPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPermissions
        fields = ['id', 'user', 'permission']


