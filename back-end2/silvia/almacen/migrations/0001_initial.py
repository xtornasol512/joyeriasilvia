# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Temporal'
        db.create_table(u'almacen_temporal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('idProv', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('idTipo', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
        ))
        db.send_create_signal(u'almacen', ['Temporal'])

        # Adding model 'Joya'
        db.create_table(u'almacen_joya', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('clave', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('proveedor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proveedores.Proveedor'], null=True, blank=True)),
            ('tipoJoya', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['almacen.TipoJoya'])),
            ('fechaCompra', self.gf('django.db.models.fields.DateField')()),
            ('peso', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=3)),
            ('costo', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('precioVentaContado', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('precioVentaPagos', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('existente', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'almacen', ['Joya'])

        # Adding model 'TipoJoya'
        db.create_table(u'almacen_tipojoya', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('clave', self.gf('django.db.models.fields.CharField')(unique=True, max_length=5)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('valor', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal(u'almacen', ['TipoJoya'])

        # Adding model 'Valor'
        db.create_table(u'almacen_valor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipoJoya', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tipo_joya', to=orm['almacen.TipoJoya'])),
            ('fecha', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('valor', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('notas', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'almacen', ['Valor'])


    def backwards(self, orm):
        # Deleting model 'Temporal'
        db.delete_table(u'almacen_temporal')

        # Deleting model 'Joya'
        db.delete_table(u'almacen_joya')

        # Deleting model 'TipoJoya'
        db.delete_table(u'almacen_tipojoya')

        # Deleting model 'Valor'
        db.delete_table(u'almacen_valor')


    models = {
        u'almacen.joya': {
            'Meta': {'object_name': 'Joya'},
            'clave': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'costo': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'existente': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'fechaCompra': ('django.db.models.fields.DateField', [], {}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'peso': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '3'}),
            'precioVentaContado': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'precioVentaPagos': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'proveedor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['proveedores.Proveedor']", 'null': 'True', 'blank': 'True'}),
            'tipoJoya': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['almacen.TipoJoya']"})
        },
        u'almacen.temporal': {
            'Meta': {'object_name': 'Temporal'},
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idProv': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'idTipo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'almacen.tipojoya': {
            'Meta': {'object_name': 'TipoJoya'},
            'clave': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '5'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'valor': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        },
        u'almacen.valor': {
            'Meta': {'object_name': 'Valor'},
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notas': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'tipoJoya': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tipo_joya'", 'to': u"orm['almacen.TipoJoya']"}),
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