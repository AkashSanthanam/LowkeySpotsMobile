from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'map_count', 'friend_count']
        extra_kwargs = {
            'password': {'write_only': True},
            'map_count': {'read_only': True},
            'friend_count': {'read_only': True},
            'id': {'read_only': True},
        }
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    