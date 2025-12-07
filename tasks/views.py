from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwner

class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):         # user sees only their own tasks
        return Task.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):         # set the task owner to the logged-in user
        serializer.save(owner=self.request.user)