from django.db import models
from apps.users.models import Users


class Notifications(models.Model):
    """
    Notifications model
    """
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    message = models.TextField()
    ship_date = models.DateTimeField()
    state = models.BooleanField(default=False)

    def __str__(self):
        return self.message
