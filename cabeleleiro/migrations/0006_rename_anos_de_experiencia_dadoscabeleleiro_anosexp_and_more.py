# Generated by Django 5.0.6 on 2024-05-21 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cabeleleiro', '0005_dadoscabeleleiro_tipocabelo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dadoscabeleleiro',
            old_name='anos_de_experiencia',
            new_name='anos_de_experiencia',
        ),
        migrations.RenameField(
            model_name='dadoscabeleleiro',
            old_name='certificado_cabeleleiro',
            new_name='certificado',
        ),
    ]