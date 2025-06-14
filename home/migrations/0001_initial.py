# Generated by Django 5.1.7 on 2025-05-31 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=0, max_digits=12)),
                ('img', models.ImageField(upload_to='picture/')),
            ],
        ),
    ]
