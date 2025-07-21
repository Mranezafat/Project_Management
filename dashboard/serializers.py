from rest_framework import serializers
from .models import Dashboard
class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        fields = ['id', 'profile', 'name', 'created_at']
        read_only_fields = ['id', 'created_at']
    