from django.urls import path, include
from .views import TodoApiView

urlpatterns = [
    path('todo/', TodoApiView.as_view(), name='todo'),
    path('todo/<int:id>/', TodoApiView.as_view(), name='todo-delete')
]
