# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255, null=True, blank=True)),
                ('direccion', models.TextField(null=True, blank=True)),
                ('correo', models.EmailField(max_length=75, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=255, null=True, blank=True)),
                ('telefono', models.CharField(max_length=20, null=True, blank=True)),
                ('proveedor', models.ForeignKey(to='proveedores.Proveedor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
