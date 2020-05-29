from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser


# Create your models here.


class VMLoan(models.Model):
    pass


class VM(models.Model):
    pass


class Purpose(models.Model):
    purposeDescription = models.CharField(max_length=200)


class ItemDescription(models.Model):
    itemDescription = models.CharField(max_length=200)


class InventoryItemType(models.Model):
    inventoryItemType = models.CharField(max_length=50)

    def __str__(self):
        return self.inventoryItemType


class ItemOS(models.Model):
    itemOS = models.CharField(max_length=50)

    def __str__(self):
        return self.itemOS


class ItemSoftware(models.Model):
    itemSoftwareName = models.CharField(max_length=50)
    itemSoftware = models.CharField(max_length=200)

    def __str__(self):
        return self.itemSoftwareName


class InventoryItem(models.Model):
    itemName = models.CharField(max_length=50)
    itemDescription = models.ForeignKey(ItemDescription, on_delete=models.CASCADE)
    itemSoftware = models.ManyToManyField(ItemSoftware)
    itemType = models.ForeignKey(InventoryItemType, on_delete=models.CASCADE)
    itemOS = models.ForeignKey(ItemOS, on_delete=models.CASCADE)
    itemAvailable = models.BooleanField()

    def __str__(self):
        return self.itemName


class Loan(models.Model):
    loanedItem = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    loanStartDate = models.DateField()
    loanEndDate = models.DateField()
    loaningUser = models.ForeignKey(User, on_delete=models.CASCADE)
    loanPurpose = models.ForeignKey(Purpose, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.loaningUser} - {self.loanedItem}"


class Reservation(models.Model):
    reservedItem = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    reservingUser = models.ForeignKey(User, on_delete=models.CASCADE)
    reservationStartDate = models.DateField(auto_now=True)
    reservationEndDate = models.DateField()
    reservedFor = models.ForeignKey(User, related_name="reservedForUser", on_delete=models.CASCADE)
    reservationPurpose = models.ForeignKey(Purpose, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.reservingUser} reserved {self.reservedItem} for {self.reservedFor}"
