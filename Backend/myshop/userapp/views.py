from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer, PasswordChangeSerializer, LogoutSerializer
from .models import LoginAttempt
from django.db import transaction
from django.utils import timezone  # Add this import
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            
            # Capture device details and IP address from the request
            device_details = request.META.get('HTTP_USER_AGENT', 'Unknown Device')
            ip_address = request.META.get('REMOTE_ADDR', 'Unknown IP')

            try:
                with transaction.atomic():
                    # Check if the user is already logged in from another device
                    existing_sessions = LoginAttempt.objects.filter(user=user, is_active=True)
                    for session in existing_sessions:
                        if session.device_details == device_details and session.ip_address == ip_address:
                            # Allow login from the same device
                            session.timestamp = timezone.now()  # Update the timestamp
                            session.save()
                            break
                    else:
                        if existing_sessions.exists():
                            return Response(
                                {"error": "You are already logged in from another device."},
                                status=status.HTTP_403_FORBIDDEN
                            )

                    # Log the current login attempt
                    LoginAttempt.objects.create(
                        user=user,
                        ip_address=ip_address,
                        device_details=device_details,
                        is_active=True,
                        successful=True  # Mark the login attempt as successful
                    )

                return Response({
                    "access": str(refresh.access_token),
                    "refresh": str(refresh),
                    "device": device_details,
                    "ip_address": ip_address,
                })
            except Exception as e:
                return Response({"error": f"An error occurred during login: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)
        except Exception:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):
        """
        Handle JSON input for updating user profiles.
        """
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """
        Handle partial updates to user profiles.
        """
        return self.partial_update(request, *args, **kwargs)

class PasswordChangeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = PasswordChangeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            request.user.set_password(serializer.validated_data['new_password'])
            request.user.save()
            return Response({"message": "Password changed successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
