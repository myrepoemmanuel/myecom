# Generated by Django 4.0.3 on 2022-04-12 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
        ('store', '0016_order_vendor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='vendor',
        ),
        migrations.AddField(
            model_name='featuredproduct',
            name='vendor',
            field=models.ManyToManyField(blank=True, to='vendors.vendor'),
        ),
    ]
