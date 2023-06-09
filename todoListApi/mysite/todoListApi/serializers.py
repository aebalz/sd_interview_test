from rest_framework import serializers
from .models import TodoList


class TodoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoList
        fields = ('id', 'title', 'content', 'detail', 'is_completed', 'createdAt', 'updatedAt')
