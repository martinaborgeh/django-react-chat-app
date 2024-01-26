from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import CustomUser


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Custom claims
        # token["username"] = user.username
        token["email"] = user.email
        return token


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    full_name = serializers.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ["id", "email", "full_name", "role"]


class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    full_name = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ("full_name", "role", "password", "password2", "email")

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            email=validated_data["email"],
            full_name=validated_data["full_name"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user
