from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import TODO
from .serializer import TodoSerializer
from .pagination import CustomPageNumberPagination

# constants
STATUS_CODE = ['COMPLETED', 'INCOMPLETE']


class TodoApiView(APIView):
    def get(self, request, id=None):
        task_id = request.query_params.get('id')
        status_code = request.query_params.get('status_code')
        todos = TODO.objects.filter(is_deleted=False)

        if task_id:
            todos = todos.filter(id=task_id)
        if id:
            todos = todos.filter(id=id)
        if status_code:
            if status_code in STATUS_CODE:
                is_completed = (status_code == 'COMPLETED')
                todos = todos.filter(is_completed=is_completed)
            else:
                return Response(
                    {"status_code": "Status code can be only 'COMPLETED' or 'INCOMPLETE'"},
                    status=status.HTTP_400_BAD_REQUEST
                )

        paginator = CustomPageNumberPagination()
        paginated_todos = paginator.paginate_queryset(todos, request)
        serialized_data = TodoSerializer(paginated_todos, many=True)

        return paginator.get_paginated_response(serialized_data.data)

    def post(self, request):
        serializedData = TodoSerializer(data=request.data)
        if serializedData.is_valid():
            serializedData.save()
            return Response(serializedData.data, status=status.HTTP_201_CREATED)
        return Response(serializedData.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        data = request.data
        id = data.get('id', None)
        if not id:
            return Response({"error": "The ID is required field "})
        todo = get_object_or_404(TODO, id=id)
        # partial=True allows partial updates
        serializer = TodoSerializer(todo, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # This is only used to hard delete the Task
    def delete(self, request, id=None):
        todo = get_object_or_404(TODO, id=id)
        todo.delete()
        return Response({"message": f'The task {id} is deleted'}, status=status.HTTP_200_OK)
