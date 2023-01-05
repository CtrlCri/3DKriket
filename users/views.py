from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken

from users.serializers import UserSerializer, AuthTokenSerializer 

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer
    
class RetrieveUpdateUserView(generics.RetrieveUpdateAPIView):
    """Retrieve and update authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user
    
class CreateTokenView(ObtainAuthToken):
    """Create a new authentication token for user"""
    serializer_class = AuthTokenSerializer

