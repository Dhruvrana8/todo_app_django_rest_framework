from django.urls import path, include
from .views import TodoApiView

urlpatterns=[
path('todo/', TodoApiView.as_view()),
]