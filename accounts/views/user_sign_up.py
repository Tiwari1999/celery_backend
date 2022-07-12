from rest_framework.viewsets import ModelViewSet

from accounts.serializers import UserSerializer


class UserSignUpViewSet(ModelViewSet):
    serializer_class = UserSerializer
