# Generated by Django 4.1.7 on 2023-04-03 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='topic_name',
            new_name='tname',
        ),
        migrations.RenameField(
            model_name='webpages',
            old_name='topic_name',
            new_name='tname',
        ),
    ]
