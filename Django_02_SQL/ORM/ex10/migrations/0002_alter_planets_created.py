# Generated by Django 5.1.5 on 2025-02-10 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex10', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planets',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
