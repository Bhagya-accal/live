# Generated by Django 5.0.1 on 2024-01-16 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('std', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='pass1',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='studentid',
            new_name='username',
        ),
    ]
