from django.db import models
from apps.users.models import Users


class Ticket(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('in_progress', 'In Progress'),
    )

    title = models.CharField(max_length=60)
    description = models.TextField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    status = models.CharField(max_length=11, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
