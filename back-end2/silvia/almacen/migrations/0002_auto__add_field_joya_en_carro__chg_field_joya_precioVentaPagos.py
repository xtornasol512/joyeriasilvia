# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Joya.en_carro'
        db.add_column(u'almacen_joya', 'en_carro',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'Joya.precioVentaPagos'
        db.alter_column(u'almacen_joya', 'precioVentaPagos', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=2))

    def backwards(self, orm):
        # Deleting field 'Joya.en_carro'
        db.delete_column(u'almacen_joya', 'en_carro')


        # Changing field 'Joya.precioVentaPagos'
        db.alter_column(u'almacen_joya', 'precioVentaPagos', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2))

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
            'en_carro': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'existente': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'fechaCompra': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'peso': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '3'}),
            'precioVentaContado': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '2', 'blank': 'True'}),
            'precioVentaPagos': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '2', 'blank': 'True'}),
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