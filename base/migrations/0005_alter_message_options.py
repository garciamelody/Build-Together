# Generated by Django 4.1.5 on 2023-01-26 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_message_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
