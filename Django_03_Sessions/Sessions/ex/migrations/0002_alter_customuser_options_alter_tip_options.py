# Generated by Django 4.2.19 on 2025-02-16 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ex', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'permissions': [('downvote_posts', 'Can downvote posts')]},
        ),
        migrations.AlterModelOptions(
            name='tip',
            options={},
        ),
    ]
