from django.contrib.auth.models import User
from django.db import models


class UserExtend(User):

    email_confirmation = models.EmailField(max_length=30)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

