# Generated by Django 5.1 on 2024-09-11 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
