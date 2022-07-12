from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet

from accounts.models import User
from accounts.serializers import UserSerializer
from realizefi_backend_django.views import SingleResourceViewSet


class IsPostOrIsAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        # allow all POST requests
        if request.method == 'POST':
            return True

        # Otherwise, only allow authenticated requests
        # Post Django 1.10, 'is_authenticated' is a read-only attribute
        return request.user and request.user.is_authenticated


class CurrentUserViewSet(ModelViewSet):

    @staticmethod
    def has_permission(request, view):
        # allow all POST requests
        if request.method == 'POST':
            return True

        # Otherwise, only allow authenticated requests
        # Post Django 1.10, 'is_authenticated' is a read-only attribute
        return request.user and request.user.is_authenticated

    authentication_classes = [TokenAuthentication]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsPostOrIsAuthenticated]

