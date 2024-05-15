from django.db import models
from apps.users.models import Users


class Permissions(models.Model):
    """
    Permission model
    """
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class UserPermissions(models.Model):
    """
    UserPermissions model
    """
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permissions, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.email} - {self.permission.name}"
