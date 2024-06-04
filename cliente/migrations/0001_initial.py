# Generated by Django 5.0.6 on 2024-06-03 12:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cabeleleiro', '0010_alter_datasabertas_data'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('A', 'Agendado'), ('F', 'Finalizado'), ('C', 'Cancelado'), ('I', 'Inicializado')], default='A', max_length=1)),
                ('link', models.URLField(blank=True, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('data_aberta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cabeleleiro.datasabertas')),
            ],
        ),
    ]
