from django.contrib.auth.models import User
from django.db import models


class UserExtend(User):

    gender_options = (('male', 'Male'), ('female', 'Female'), ('other', 'Other'))
    account_options = (('buyer', 'Buyer'), ('seller', 'Seller'))

    firstname = models.CharField(max_length=20, null=False)
    lastname = models.CharField(max_length=20, null=False)
    email_address = models.EmailField(max_length=30)
    phone = models.CharField(max_length=10)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=gender_options, max_length=6, null=True)
    account = models.CharField(choices=account_options, max_length=6, null=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

