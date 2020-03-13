from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Names(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class UserTypes(models.Model):
    userType = models.CharField(max_length=50)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userType = models.ForeignKey(UserTypes, on_delete=models.CASCADE)
    Name = models.ForeignKey(Names, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


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


class ItemDesciption(models.Model):
    pass


class InventoryItemType(models.Model):
    pass


class ItemOS(models.Model):
    itemOS = models.CharField(max_length=50)


class InventoryItems(models.Model):
    itemName = models.CharField(max_length=50)
    itemmDescription = models.ForeignKey(ItemDesciption, on_delete=models.CASCADE)
    itemType = models.ForeignKey(InventoryItemType, on_delete=models.CASCADE)
    itemOS = models.ForeignKey(ItemOS, on_delete=models.CASCADE)
    itemAvailable = models.BooleanField()


class InventoryItems_has_ItemSoftware(models.Model):
    pass


class ItemSoftware(models.Model):
    pass
