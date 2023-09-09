from rest_framework import serializers

from authentications.models import User


# password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username", "email", "password", "phone_number"
        ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = [
            "email", "password"
        ]


class LogoutSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = [
            "email"
        ]
