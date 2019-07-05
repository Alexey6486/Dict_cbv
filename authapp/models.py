from django.db import models

from django.contrib.auth.models import User, AbstractUser
from django.utils.timezone import now
from datetime import timedelta


# Create your models here.


class DictUser(AbstractUser):

    # class Meta(object):
    #     unique_together = ('email',)

    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'M'),
        (FEMALE, 'W'),
    )

    gender = models.CharField(verbose_name='gender', max_length=1, choices=GENDER_CHOICES, blank=True)
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='age', default=18)
    # activation_key = models.CharField(verbose_name='key conformation', max_length=128, blank=True)
    # activation_key_expires = models.DateTimeField(
    #     verbose_name='key relevance',
    #     default=(now() + timedelta(hours=48)))
    #
    # def is_activation_key_expired(self):
    #     if now() <= self.activation_key_expires:
    #         return False
    #     else:
    #         return True
