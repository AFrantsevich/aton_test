from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True,
                                on_delete=models.CASCADE,
                                related_name='userprofile')
    phone = models.CharField(max_length=20, blank=True)
    middle_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return (f'{self.user.first_name}'
                f' {self.middle_name} {self.user.last_name}')


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)


post_save.connect(create_user_profile, sender=User)
