from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    email = models.EmailField('Email поле', unique=True)
    username = models.CharField('Нік користувача', max_length=150)
    is_editor = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return f'User {self.username}'
  

@receiver(post_save, sender=User)
def superuser_also_editor(sender, instance, **kwargs):
    if not instance.is_editor and instance.is_superuser:
        instance.is_editor = True
        instance.save()


