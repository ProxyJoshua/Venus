# Generated by Django 3.0.1 on 2020-01-07 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0004_auto_20191220_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='carro',
            name='estado',
            field=models.CharField(default='espera', max_length=200),
            preserve_default=False,
        ),
    ]
