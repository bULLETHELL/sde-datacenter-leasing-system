# Generated by Django 3.0.6 on 2020-05-29 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200528_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitemtype',
            name='pp',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]