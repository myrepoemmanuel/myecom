# Generated by Django 3.2.5 on 2022-05-20 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_delete_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[(1, 'Apparel'), (2, 'Footware'), (3, 'Bags'), (4, 'Accessories'), (5, 'Eyewear'), (6, 'Cosmetics and Beauty'), (7, 'Consumer Electronics'), (8, 'Sporting goods')], max_length=200, null=True)),
            ],
        ),
    ]
