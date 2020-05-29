# Generated by Django 3.0.6 on 2020-05-29 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_itemdescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='itemDescription',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.ItemDescription'),
            preserve_default=False,
        ),
    ]
