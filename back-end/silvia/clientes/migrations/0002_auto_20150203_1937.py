# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Deuda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deuda', models.DecimalField(max_digits=9, decimal_places=2)),
                ('cliente', models.ForeignKey(to='clientes.Cliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistorialPago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(auto_now=True)),
                ('abono', models.DecimalField(max_digits=8, decimal_places=2)),
                ('cliente', models.ForeignKey(to='clientes.Cliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='tipousuario',
            name='asignacion',
        ),
        migrations.DeleteModel(
            name='Rol',
        ),
        migrations.RemoveField(
            model_name='tipousuario',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='TipoUsuario',
        ),
    ]
