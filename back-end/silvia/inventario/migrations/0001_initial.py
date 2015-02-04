# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Joya',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clave', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=150, null=True, blank=True)),
                ('foto', models.ImageField(null=True, upload_to=b'asets/items/joyas', blank=True)),
                ('peso', models.DecimalField(max_digits=9, decimal_places=3)),
                ('costo', models.DecimalField(max_digits=9, decimal_places=2)),
                ('precioOroCompra', models.DecimalField(max_digits=5, decimal_places=2)),
                ('fechaCompra', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Kilataje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kilataje', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoOro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=255)),
                ('precioActual', models.DecimalField(max_digits=6, decimal_places=2)),
            ],
            options={
                'verbose_name': 'Tipo deOro',
                'verbose_name_plural': 'Tipos de Oro',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='joya',
            name='kilataje',
            field=models.ForeignKey(blank=True, to='inventario.Kilataje', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='joya',
            name='proveedor',
            field=models.ForeignKey(to='proveedores.Proveedor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='joya',
            name='tipoOro',
            field=models.ForeignKey(blank=True, to='inventario.TipoOro', null=True),
            preserve_default=True,
        ),
    ]
