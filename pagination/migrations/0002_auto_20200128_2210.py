# Generated by Django 3.0 on 2020-01-28 22:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagination', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='due_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='name',
            field=models.CharField(blank=True, choices=[('user1', 'user1'), ('user2', 'user2')], max_length=50),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='text',
            field=models.TextField(blank=True, default='something something ...'),
        ),
    ]
