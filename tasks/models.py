from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = [
        ('todo','To Do'),
        ('in_progress','In Progress'),
        ('done','Done'),
    ]

    PRIORITY_CHOICES = [
        ('low','Low'),
        ('medium','Medium'),
        ('high','High'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(Self):
        return Self.title
