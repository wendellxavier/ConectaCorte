# Generated by Django 5.0.6 on 2024-05-19 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cabeleleiro', '0003_tipocabelos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tipocabelos',
            old_name='tipoCabelos',
            new_name='tipoCabelo',
        ),
    ]