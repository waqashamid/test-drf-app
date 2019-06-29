from rest_framework import viewsets, permissions

from accounts.serializers import UserRegistrationSerializer


class UserRegistrationView(viewsets.ModelViewSet):
    """
    UserRegistrationView
        A view to handle the User registration process
    """
    permission_classes = (
        permissions.AllowAny,
    )

    serializer_class = UserRegistrationSerializer