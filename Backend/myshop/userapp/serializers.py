# from rest_framework import serializers
# from .models import User, LoginAttempt


# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(
#         write_only=True,
#         min_length=8,
#         help_text="Password must be at least 8 characters long."
#     )

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password', 'role', 'profile_picture']
#         extra_kwargs = {
#             'username': {'help_text': 'Unique username for the user.'},
#             'email': {'help_text': 'Email address of the user.'},
#             'role': {'help_text': 'Role of the user (admin, staff, user).'},
#             'profile_picture': {'help_text': 'Optional profile picture for the user.'},
#         }

#     def validate_email(self, value):
#         if User.objects.filter(email=value).exists():
#             raise serializers.ValidationError("A user with this email already exists.")
#         return value

#     def create(self, validated_data):
#         user = User.objects.create_user(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             password=validated_data['password'],
#             role=validated_data.get('role', 'user'),
#             profile_picture=validated_data.get('profile_picture')
#         )
#         user.is_email_verified = False
#         user.save()
#         return user


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'role', 'profile_picture', 'is_email_verified']
#         read_only_fields = ['is_email_verified']


# class LoginAttemptSerializer(serializers.ModelSerializer):
#     user = serializers.StringRelatedField(read_only=True)

#     class Meta:
#         model = LoginAttempt
#         fields = ['user', 'timestamp', 'successful']
#         read_only_fields = ['user', 'timestamp', 'successful']



from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import check_password

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'role')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid email or password.")

        if not check_password(password, user.password):
            raise serializers.ValidationError("Invalid email or password.")

        if not user.is_active:
            raise serializers.ValidationError("User account is disabled.")

        data["user"] = user
        return data

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'role', 'profile_picture')

class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    def validate(self, data):
        user = self.context['request'].user
        if not user.check_password(data['old_password']):
            raise serializers.ValidationError("Old password is incorrect.")
        return data

class LogoutSerializer(serializers.Serializer):
    pass  # No extra fields needed for logout
