# Generated by Django 4.2.4 on 2023-08-17 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_alter_task_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_name',
            field=models.CharField(default='', max_length=20, null=True),
        ),
    ]
