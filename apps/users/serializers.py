from rest_framework import serializers
from .models import Users


class UserSerializer(serializers.ModelSerializer):
    """
    User serializer
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        """
        Meta class
        """
        model = Users
        fields = ['id', 'name', 'email',
                  'password', 'is_staff', 'is_superuser']

    def create(self, validated_data):
        """
        Create a user with the given data and hash the password
        """
        password = validated_data.pop('password', None)
        user = Users(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        """
        Update the user
        """
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance
