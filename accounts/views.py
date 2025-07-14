from rest_framework import generics
from .serializers import UserRegisterSerializer, UserLoginSerializer
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login,logout
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.core.exceptions import ValidationError
from django.db import IntegrityError
class UserRegisterPageView(TemplateView):
    template_name = 'register.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().get(request, *args, **kwargs)
    
class UserRegisterAPIView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
class UserLoginAPIView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return Response({"message": "Login successful", "user": user.username})
        else:
            print("Validation errors:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
        
class UserLoginPageView(TemplateView):
    template_name = 'login.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().get(request, *args, **kwargs)
    
@method_decorator(csrf_exempt, name='dispatch')
class UserLogoutAPIView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({"error": "You are not logged in."}, status=status.HTTP_401_UNAUTHORIZED)
        logout(request)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
class UserLogoutPageView(TemplateView):
    template_name = 'logout.html'