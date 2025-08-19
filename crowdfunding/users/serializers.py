from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'  # This will include all fields defined in the CustomUser model
        extra_kwargs = {'password': {'write_only': True}} # Ensure password is write-only for security

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data) # Use create_user to handle password hashing ** deals with kwargs