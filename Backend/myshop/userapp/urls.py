# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import RegisterViewSet, ProfileViewSet, LoginAttemptViewSet

# router = DefaultRouter()
# router.register(r'register', RegisterViewSet, basename='register')
# router.register(r'profile', ProfileViewSet, basename='profile')
# router.register(r'login-attempts', LoginAttemptViewSet, basename='login-attempts')

# urlpatterns = [
#     path('', include(router.urls)),
# ]
from django.urls import path
from .views import RegisterView, LoginView, LogoutView, ProfileView, PasswordChangeView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('change-password/', PasswordChangeView.as_view(), name='change_password'),
]
