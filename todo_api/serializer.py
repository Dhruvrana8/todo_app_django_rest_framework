from rest_framework import serializers
from .models import TODO


class TodoSerializer(serializers.ModelSerializer):
    task_title = serializers.CharField(max_length=100, required=True)

    class Meta:
        model = TODO
        fields = ['id', 'pk', 'task_title', 'created_at',
                  'is_completed', 'is_deleted', 'task_description']
