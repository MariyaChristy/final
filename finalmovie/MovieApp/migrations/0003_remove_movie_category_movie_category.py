# Generated by Django 5.0.3 on 2024-03-07 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieApp', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='category',
        ),
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.ManyToManyField(to='MovieApp.categorymovie'),
        ),
    ]
