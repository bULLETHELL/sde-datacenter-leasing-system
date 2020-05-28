from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Names(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)


class VMLoans(models.Model):
    pass


class VMs(models.Model):
    pass


class Purposes(models.Model):
    purposeDescription = models.CharField(max_length=200)


class ItemDescription(models.Model):
    itemDescription = models.CharField(max_length=200)


class InventoryItemType(models.Model):
    inventoryItemType = models.CharField(max_length=50)


class ItemOS(models.Model):
    itemOS = models.CharField(max_length=50)


class InventoryItems(models.Model):
    itemName = models.CharField(max_length=50)
    itemDescription = models.ForeignKey(ItemDescription, on_delete=models.CASCADE)
    itemType = models.ForeignKey(InventoryItemType, on_delete=models.CASCADE)
    itemOS = models.ForeignKey(ItemOS, on_delete=models.CASCADE)
    itemAvailable = models.BooleanField()


class InventoryItems_has_ItemSoftware(models.Model):
    pass


class ItemSoftware(models.Model):
    itemSoftware = models.CharField(max_length=200)


class Loans(models.Model):
    loanedItem = models.ForeignKey(InventoryItems, on_delete=models.CASCADE)
    loanStartDate = models.DateField()
    loanEndDate = models.DateField()
    loaningUser = models.ForeignKey(User, on_delete=models.CASCADE)
    loanPurpose = models.ForeignKey(Purposes, on_delete=models.CASCADE)


class Reservations(models.Model):
    reservedItem = models.ForeignKey(InventoryItems, on_delete=models.CASCADE)
    reservingUser = models.ForeignKey(User, on_delete=models.CASCADE)
    reservationStartDate = models.DateField(auto_now=True)
    reservationEndDate = models.DateField()
    reservedFor = models.ForeignKey(User, related_name="reservedForUser", on_delete=models.CASCADE)
    reservationPurpose = models.ForeignKey(Purposes, on_delete=models.CASCADE)
