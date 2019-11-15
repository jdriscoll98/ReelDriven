from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Client(models.Model):
    CHOICES = [
        ('fitness', 'fitness',),
        ('nutrition', 'nutrition',),
        ('mindset', 'mindset',)
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_priority = models.CharField(max_length=100, choices=CHOICES, blank=True, null=True)
    second_priority = models.CharField(max_length=100, choices=CHOICES, blank=True, null=True)
    third_priority = models.CharField(max_length=100, choices=CHOICES, blank=True, null=True)


    def __str__(self):
        return self.user.first_name + self.user.last_name

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Client.objects.create(user=instance)
    instance.client.save()
