# Generated by Django 2.2.1 on 2019-05-31 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='email',
            new_name='eemail',
        ),
    ]
