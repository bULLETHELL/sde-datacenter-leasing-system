from django.contrib import admin
from django.contrib.auth.models import User
from .models import InventoryItem, InventoryItemType, ItemDescription, ItemOS, ItemSoftware, Loan, Purpose, \
    Reservation

# admin.site.register(User)

admin.site.register(InventoryItem)
admin.site.register(InventoryItemType)
admin.site.register(ItemDescription)
admin.site.register(ItemOS)
admin.site.register(ItemSoftware)
admin.site.register(Loan)
admin.site.register(Purpose)
admin.site.register(Reservation)
