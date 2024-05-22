from django.db import migrations, models
from django.db.models.deletion import DO_NOTHING

class Migration(migrations.Migration):

    dependencies = [
        ('cabeleleiro', '0004_rename_tipocabelos_tipocabelos_tipocabelo'),
    ]

    def set_default_tipo_cabelo(apps, schema_editor):
        TipoCabelos = apps.get_model('cabeleleiro', 'TipoCabelos')
        default_tipo_cabelo = TipoCabelos.objects.first()  
        DadosCabeleleiro = apps.get_model('cabeleleiro', 'DadosCabeleleiro')
        DadosCabeleleiro.objects.all().update(tipoCabelo=default_tipo_cabelo)

    operations = [
        migrations.AddField(
            model_name='dadoscabeleleiro',
            name='tipoCabelo',
            field=models.ForeignKey(on_delete=DO_NOTHING, to='cabeleleiro.TipoCabelos'),
        ),
        migrations.RunPython(set_default_tipo_cabelo),  
    ]
