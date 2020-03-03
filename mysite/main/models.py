from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class UserTypes(models.Model):
    pass


class VMLoans(models.Model):
    pass


class VMs(models.Model):
    pass


class Reservations(models.Model):
    pass


class Purposes(models.Model):
    pass


class Loans(models.Model):
    pass


class InventoryItems(models.Model):
    pass


class InventoryItems_has_ItemSoftware(models.Model):
    pass


class InventoryItemType(models.Model):
    pass


class ItemOS(models.Model):
    pass


class ItemDesciption(models.Model):
    pass


class ItemSoftware(models.Model):
    pass
