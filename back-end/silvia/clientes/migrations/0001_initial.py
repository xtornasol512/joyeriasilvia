# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cliente'
        db.create_table(u'clientes_cliente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'clientes', ['Cliente'])

        # Adding model 'HistorialPago'
        db.create_table(u'clientes_historialpago', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Cliente'])),
            ('fecha', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('abono', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal(u'clientes', ['HistorialPago'])

        # Adding model 'Deuda'
        db.create_table(u'clientes_deuda', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Cliente'])),
            ('deuda', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
        ))
        db.send_create_signal(u'clientes', ['Deuda'])


    def backwards(self, orm):
        # Deleting model 'Cliente'
        db.delete_table(u'clientes_cliente')

        # Deleting model 'HistorialPago'
        db.delete_table(u'clientes_historialpago')

        # Deleting model 'Deuda'
        db.delete_table(u'clientes_deuda')


    models = {
        u'clientes.cliente': {
            'Meta': {'object_name': 'Cliente'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'clientes.deuda': {
            'Meta': {'object_name': 'Deuda'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Cliente']"}),
            'deuda': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'clientes.historialpago': {
            'Meta': {'object_name': 'HistorialPago'},
            'abono': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Cliente']"}),
            'fecha': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['clientes']