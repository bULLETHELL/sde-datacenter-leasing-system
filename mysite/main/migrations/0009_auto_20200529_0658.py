# Generated by Django 3.0.6 on 2020-05-29 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200529_0658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventoryitemtype',
            old_name='InventoryItemType',
            new_name='inventoryItemType',
        ),
    ]
