# Generated by Django 4.0.3 on 2022-04-12 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_remove_order_vendor_featuredproduct_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='productId',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
