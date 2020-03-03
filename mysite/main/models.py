from django.db import models


# Create your models here.
class Names(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)


class Users(models.Model):
    username = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)


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
