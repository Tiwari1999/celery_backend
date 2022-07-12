from rest_framework.exceptions import APIException
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from accounts.models import User
from accounts.serializers import UserSerializer


class UserAuthenticationViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    @action(methods=['get'], detail=False, url_path='')
    def signin(self, request, *args, **kwargs):
        if 'email' not in request.data or 'password' not in request.data:
            raise APIException(detail="email and password both are required for authentication")
        user = User.objects.filter(email=request.data['email'], password=request.data['password']).first()
        if user:
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        else:
            raise APIException(detail="authentication failed")
