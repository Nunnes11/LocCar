# Generated by Django 4.2.8 on 2023-12-14 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluguel', '0003_remove_cliente_cpf_cliente_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='ano',
            field=models.IntegerField(verbose_name='Ano do carro'),
        ),
    ]