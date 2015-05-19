# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Deuda'
        db.create_table(u'pagos_deuda', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'pagos', ['Deuda'])

        # Adding model 'ListaVenta'
        db.create_table(u'pagos_listaventa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('deuda', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pagos.Deuda'])),
            ('venta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ventas.Venta'])),
        ))
        db.send_create_signal(u'pagos', ['ListaVenta'])

        # Adding model 'HistorialPago'
        db.create_table(u'pagos_historialpago', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('deuda', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pagos.Deuda'])),
            ('abono', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('fecha', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('notas', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'pagos', ['HistorialPago'])


    def backwards(self, orm):
        # Deleting model 'Deuda'
        db.delete_table(u'pagos_deuda')

        # Deleting model 'ListaVenta'
        db.delete_table(u'pagos_listaventa')

        # Deleting model 'HistorialPago'
        db.delete_table(u'pagos_historialpago')


    models = {
        u'clientes.cliente': {
            'Meta': {'object_name': 'Cliente'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notas': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'pagos.deuda': {
            'Meta': {'object_name': 'Deuda'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'pagos.historialpago': {
            'Meta': {'object_name': 'HistorialPago'},
            'abono': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'deuda': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pagos.Deuda']"}),
            'fecha': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notas': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'pagos.listaventa': {
            'Meta': {'object_name': 'ListaVenta'},
            'deuda': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pagos.Deuda']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'venta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ventas.Venta']"})
        },
        u'ventas.venta': {
            'Meta': {'object_name': 'Venta'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Cliente']"}),
            'contado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fecha': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notas': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'total': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'})
        }
    }

    complete_apps = ['pagos']