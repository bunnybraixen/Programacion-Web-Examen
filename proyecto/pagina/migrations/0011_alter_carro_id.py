# Generated by Django 4.2.13 on 2024-06-24 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0010_usuario_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
