from django.urls import path
from .views import   HomeApiView

urlpatterns = [
    path('', HomeApiView.as_view(), name='home-api'),
]