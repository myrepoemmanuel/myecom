# Generated by Django 3.2.5 on 2022-08-10 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0026_auto_20220623_0930'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.categories')),
            ],
        ),
    ]
