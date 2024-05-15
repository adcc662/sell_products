from django.db import models
from apps.users.models import Users


class Profile(models.Model):
    """
    Profile model
    """
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
