# Generated by Django 4.2.13 on 2024-06-24 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0011_alter_carro_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carro',
            old_name='id',
            new_name='id2',
        ),
    ]