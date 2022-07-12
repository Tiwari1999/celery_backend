from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from accounts.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(ModelSerializer):
    user_token = serializers.SerializerMethodField()

    @staticmethod
    def get_user_token(user: User):
        return str(Token.objects.filter(user=user).first())

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = (
            'first_name', 'last_name', 'email', 'password',
        )
