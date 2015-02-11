# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Joya'
        db.create_table(u'inventario_joya', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('clave', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('peso', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=3)),
            ('kilataje', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventario.Kilataje'], null=True, blank=True)),
            ('tipoOro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventario.TipoOro'], null=True, blank=True)),
            ('proveedor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proveedores.Proveedor'])),
            ('costo', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('precioOroCompra', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('fechaCompra', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'inventario', ['Joya'])

        # Adding model 'Kilataje'
        db.create_table(u'inventario_kilataje', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('kilataje', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'inventario', ['Kilataje'])

        # Adding model 'TipoOro'
        db.create_table(u'inventario_tipooro', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('precioActual', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
        ))
        db.send_create_signal(u'inventario', ['TipoOro'])


    def backwards(self, orm):
        # Deleting model 'Joya'
        db.delete_table(u'inventario_joya')

        # Deleting model 'Kilataje'
        db.delete_table(u'inventario_kilataje')

        # Deleting model 'TipoOro'
        db.delete_table(u'inventario_tipooro')


    models = {
        u'inventario.joya': {
            'Meta': {'object_name': 'Joya'},
            'clave': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'costo': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'fechaCompra': ('django.db.models.fields.DateField', [], {}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kilataje': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventario.Kilataje']", 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'peso': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '3'}),
            'precioOroCompra': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'proveedor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['proveedores.Proveedor']"}),
            'tipoOro': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventario.TipoOro']", 'null': 'True', 'blank': 'True'})
        },
        u'inventario.kilataje': {
            'Meta': {'object_name': 'Kilataje'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kilataje': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'inventario.tipooro': {
            'Meta': {'object_name': 'TipoOro'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precioActual': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'})
        },
        u'proveedores.proveedor': {
            'Meta': {'object_name': 'Proveedor'},
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['inventario']