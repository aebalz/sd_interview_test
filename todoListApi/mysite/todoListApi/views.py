from django.shortcuts import render
from .models import TodoList
from rest_framework import generics
from .serializers import TodoListSerializer


# Create your views here.
class GetTodoList(generics.ListCreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

    # return Response(queryset.data)


class GetTodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
