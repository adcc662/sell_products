from rest_framework import serializers
from .models import Notifications
import datetime


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = ['id', 'user', 'message', 'ship_date', 'state']

    def validate_ship_date(self, value):
        """
        Check that the ship date is not in the past.
        """
        if value < datetime.datetime.now(value.tzinfo):
            raise serializers.ValidationError("Ship date cannot be in the past")
        return value
