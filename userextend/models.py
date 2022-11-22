from django.contrib.auth.models import User
from django.db import models


class UserExtend(User):

    gender_options = (('male', 'Male'), ('female', 'Female'), ('other', 'Other'))

    firstname = models.CharField(max_length=20, null=False)
    lastname = models.CharField(max_length=20, null=False)
    email_address = models.EmailField(max_length=30)
    phone = models.CharField(max_length=10)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=gender_options, max_length=6, null=True)
    seller = models.BooleanField(default=False)
    buyer = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

