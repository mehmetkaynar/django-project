# Generated by Django 5.0.6 on 2024-05-18 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_adi', models.CharField(max_length=200)),
                ('aciklama', models.TextField()),
                ('image', models.CharField(max_length=100)),
                ('anasayfa', models.BooleanField(default=False)),
            ],
        ),
    ]
