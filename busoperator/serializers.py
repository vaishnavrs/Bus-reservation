from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import Bus


class UserSer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','username','password']
        
    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data)
    
class BusSer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Bus
        fields='__all__'
    