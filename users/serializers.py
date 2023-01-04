from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object"""

    class Meta:
        model = get_user_model()
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)
    
    def update(self, instance, validated_data):
        """Update user, setting the password correctly and return it"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        
        if password:
            if self.context['request'].user != instance:
                raise serializers.ValidationError('You are not allowed to update the password for this user')
            user.set_password(password)
            user.save()
        
        return user
    
class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})
    
    def validate(self, data):
        """Validate and authenticate the user"""
        email = data.get('email')
        password = data.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        
        if not user:
            raise serializers.ValidationError('authentication failed', code='authorization')
        
        if not user.is_active:
            raise serializers.ValidationError('This user is no longer active')
        
        data['user'] = user
        return data
