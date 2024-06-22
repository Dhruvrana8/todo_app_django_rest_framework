from rest_framework import serializers
from .models import TODO


class TodoSerializer(serializers.ModelSerializer):
    task = serializers.CharField(max_length=100, required=True)
    class Meta:
        model = TODO
        fields = ['id', 'task', 'created_at','is_completed','is_deleted']
        