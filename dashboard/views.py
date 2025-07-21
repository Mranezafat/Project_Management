from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Dashboard
from rest_framework import generics
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from .serializers import DashboardSerializer

class DashboardMainView(TemplateView):
    template_name = 'main.html'
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().get(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dashboards'] = Dashboard.objects.filter(profile=self.request.user.profile)
        context['username'] = User.objects.get(username=self.request.user.username)
        return context
class HomeMainView(TemplateView):
    template_name='home.html'
class HomeApiView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"message": "Welcome to the Dashboard API"}, status=status.HTTP_200_OK)
