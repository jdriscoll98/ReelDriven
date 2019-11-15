from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=200)

    def __str__(self):
        return self.user.first_name + self.user.last_name
