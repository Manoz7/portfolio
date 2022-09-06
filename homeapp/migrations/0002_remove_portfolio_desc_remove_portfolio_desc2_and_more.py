# Generated by Django 4.1 on 2022-09-06 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='desc2',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='content',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='published_date',
            field=models.DateField(default='2022-02-02'),
        ),
    ]