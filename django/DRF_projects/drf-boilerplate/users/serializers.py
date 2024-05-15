from rest_framework import serializers
import re

from users.models import User


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=100, min_length=8)
    # not displaying password in response
    password = serializers.CharField(max_length=200, write_only=True)

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email", "password")

    def validate_email(self, value):
        if User.objects.filter(email__icontains=value).exists():
            raise serializers.ValidationError({"email": "email is already taken"})
        return value

    def validate_password(self, value):
        if not value:
            raise serializers.ValidationError({"password": "password is required"})
        # Regular expression to check for at least 8 characters, one number, one letter, and one special character
        pattern = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
        result = re.match(pattern, value)

        if result is None:
            raise serializers.ValidationError(
                {
                    "password": "Password must be at least 8 characters long, include at least one number, one letter, and one special character."
                }
            )
        return value

    def create(self, validated):
        return User.objects.create_user(**validated)
