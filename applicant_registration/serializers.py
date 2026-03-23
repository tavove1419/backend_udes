from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .services.session_service import create_session
from .models import User, Application, Registration, Session, Notification

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'last_name', 'email', 'phone','role']

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
    
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'

class NotifacationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class CustomTokenSerializer(TokenObtainPairSerializer):

    username_field = 'email'

    def validate(self, attrs):
        attrs['username'] = attrs.get('email')
        try:
            data = super().validate(attrs)
        except Exception:
            raise serializers.ValidationError({
                "error": "Datos de inicio de sesión inválidos"
            })
        user = self.user
        create_session(user)
        data['user'] = {
            'id': str(self.user.id),
            'email': self.user.email,
            'role': self.user.role
        }

        return data

class ApplicationListSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name')
    user_last_name = serializers.CharField(source='user.last_name')
    user_email = serializers.EmailField(source='user.email')

    class Meta:
        model = Application
        fields = [
            'id',
            'program',
            'applicant_type',
            'status',
            'created_at',
            'user_name',
            'user_last_name',
            'user_email'
        ]