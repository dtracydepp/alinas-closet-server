# Generated by Django 3.2.4 on 2021-06-15 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alinasclosetapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='piece',
            old_name='category_name',
            new_name='category',
        ),
    ]