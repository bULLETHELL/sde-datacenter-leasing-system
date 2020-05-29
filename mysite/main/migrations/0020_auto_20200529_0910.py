# Generated by Django 3.0.6 on 2020-05-29 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_itemsoftware_itemsoftwarename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventoryitem',
            name='itemSoftware',
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='itemSoftware',
            field=models.ManyToManyField(to='main.ItemSoftware'),
        ),
    ]