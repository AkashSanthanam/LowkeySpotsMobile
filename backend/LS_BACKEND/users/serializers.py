from rest_framework import serializers
from .models import LowkeyUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LowkeyUser
        fields = ['id', 'username', 'email', 'password', 'map_count', 'friend_count']
        extra_kwargs = {
            'password': {'write_only': True},
            'map_count': {'read_only': True},
            'friend_count': {'read_only': True},
            'id': {'read_only': True},
        }
            
    def create(self, validated_data):
        return LowkeyUser.objects.create_user(**validated_data)
    
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        password = validated_data.get('password')
        if password:
            instance.set_password(password)
        instance.save()
        return instance
    
    