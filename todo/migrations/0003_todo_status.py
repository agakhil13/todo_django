# Generated by Django 4.0.1 on 2022-04-22 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_user_name_alter_todo_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
