from rest_framework import serializers

from accounts.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):

    mobile_number = serializers.CharField(required=True, min_length=10, max_length=10)
    password = serializers.CharField(required=True, min_length=6, max_length=20)

    class Meta:
        model = User
        fields = (
            'mobile_number',
            'password',
        )