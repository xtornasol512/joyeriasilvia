# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Joya'
        db.create_table(u'almacen_joya', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('proveedor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proveedores.Proveedor'], null=True, blank=True)),
            ('tipoValor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['almacen.TipoValor'])),
            ('fechaCompra', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('peso', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=3)),
            ('costo', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('precioVentaContado', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=2, blank=True)),
            ('precioVentaPagos', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('existente', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('valorGO', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=2, blank=True)),
        ))
        db.send_create_signal(u'almacen', ['Joya'])

        # Adding model 'TipoValor'
        db.create_table(u'almacen_tipovalor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('clave', self.gf('django.db.models.fields.CharField')(unique=True, max_length=5)),
            ('kilataje', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('valor', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=254)),
        ))
        db.send_create_signal(u'almacen', ['TipoValor'])

        # Adding model 'HistorialValor'
        db.create_table(u'almacen_historialvalor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipoValor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tipo_valor', to=orm['almacen.TipoValor'])),
            ('fecha', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('valor', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal(u'almacen', ['HistorialValor'])


    def backwards(self, orm):
        # Deleting model 'Joya'
        db.delete_table(u'almacen_joya')

        # Deleting model 'TipoValor'
        db.delete_table(u'almacen_tipovalor')

        # Deleting model 'HistorialValor'
        db.delete_table(u'almacen_historialvalor')


    models = {
        u'almacen.historialvalor': {
            'Meta': {'object_name': 'HistorialValor'},
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipoValor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tipo_valor'", 'to': u"orm['almacen.TipoValor']"}),
            'valor': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        },
        u'almacen.joya': {
            'Meta': {'object_name': 'Joya'},
            'costo': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'existente': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'fechaCompra': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'peso': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '3'}),
            'precioVentaContado': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '2', 'blank': 'True'}),
            'precioVentaPagos': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'proveedor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['proveedores.Proveedor']", 'null': 'True', 'blank': 'True'}),
            'tipoValor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['almacen.TipoValor']"}),
            'valorGO': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '2', 'blank': 'True'})
        },
        u'almacen.tipovalor': {
            'Meta': {'object_name': 'TipoValor'},
            'clave': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kilataje': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'valor': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        },
        u'proveedores.proveedor': {
            'Meta': {'object_name': 'Proveedor'},
            'clave': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4'}),
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['almacen']