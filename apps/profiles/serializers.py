from rest_framework import serializers
from .models import Profile
from apps.users.models import Users
from apps.users.serializers import UserSerializer


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['user', 'name', 'description']

    def create(self, validated_data):
        user_data = self.context['request'].user
        profile = Profile.objects.create(user=user_data, **validated_data)
        return profile

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.save()
        return instance
