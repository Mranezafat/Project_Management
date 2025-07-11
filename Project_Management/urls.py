"""
URL configuration for Project_Management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from accounts.views import UserRegisterAPIView, UserRegisterPageView, UserLoginAPIView, UserLoginPageView, UserLogoutAPIView, UserLogoutPageView
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    # API endpoint for user registration
    # This will handle the registration of new users via a REST API
    path('api/register/', UserRegisterAPIView.as_view(), name='api_register'),
    path('register/', UserRegisterPageView.as_view(), name='register'),
    path('api/login/', UserLoginAPIView.as_view(), name='api_login'),
    path('login/', UserLoginPageView.as_view(), name='login'),
    path('api/logout/', UserLogoutAPIView.as_view(), name='api_logout'),
    path('logout/', UserLogoutPageView.as_view(), name='logout'),
]