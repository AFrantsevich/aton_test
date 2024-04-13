from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    class Status(models.IntegerChoices):
        WORK = 0,
        REJECT = 1,
        CLOSE = 2,
        NOT_WORK = 3

    bank_account_number = models.CharField(max_length=24)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField()
    inn = models.CharField(max_length=14)
    response_person = models.ManyToManyField(User, related_name='clients')
    status = models.SmallIntegerField(
        choices=Status,
        default=Status.NOT_WORK,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
