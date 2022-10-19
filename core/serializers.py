from djoser.serializers import UserCreateSerializer as BaserUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers

class UserCreateSerializer(BaserUserCreateSerializer):
    class Meta(BaserUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name'] 

class UserSerializer(BaserUserCreateSerializer):
    class Meta(BaserUserCreateSerializer.Meta):
        fields = ['id', 'email', 'username', 'first_name', 'last_name']