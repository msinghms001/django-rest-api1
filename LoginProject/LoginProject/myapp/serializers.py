from rest_framework.serializers import Serializer,ModelSerializer

from django.contrib.auth.models import User

class SignupSer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username','password']
# User Serializer
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user


