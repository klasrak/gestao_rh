# Generated by Django 2.1 on 2019-02-26 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0003_auto_20190225_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='empresas.Empresa'),
        ),
    ]