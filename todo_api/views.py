from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import TODO
from .serializer import TodoSerializer

# Create your views here.

class TodoApiView(APIView):
    def get(self,request):
        data = TODO.objects.all()
        serializedData = TodoSerializer(data, many=True)
        return Response(serializedData.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializedData = TodoSerializer(data=request.data)
        if serializedData.is_valid():
            serializedData.save()
            return Response(serializedData.data, status=status.HTTP_201_CREATED)
        return Response(serializedData.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request):
        data = request.data
        id = data.get('id', None)
        if not id:
            return Response(
                {"error":"The Id is required field "}
            )
        
        todo = get_object_or_404(TODO, id=id)
        serializer = TodoSerializer(todo, data=data, partial=True)  # partial=True allows partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        