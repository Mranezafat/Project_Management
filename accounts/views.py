from rest_framework import generics
from .serializers import UserRegisterSerializer, UserLoginSerializer
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework import status
class UserRegisterPageView(TemplateView):
    template_name = 'register.html'
class UserRegisterAPIView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
class UserLoginAPIView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            return Response({"message": "Login successful", "user": user.username})
        else:
            print("Validation errors:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
class UserLoginPageView(TemplateView):
    template_name = 'login.html'
