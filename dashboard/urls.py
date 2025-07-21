from django.urls import path
from .views import DashboardMainView, HomeApiView

urlpatterns = [
    path('', DashboardMainView.as_view(), name='dashboard'),
    path('api/home/', HomeApiView.as_view(), name='home-api'),
]