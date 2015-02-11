# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Proveedor'
        db.create_table(u'proveedores_proveedor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('direccion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('correo', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
        ))
        db.send_create_signal(u'proveedores', ['Proveedor'])

        # Adding model 'Telefono'
        db.create_table(u'proveedores_telefono', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('proveedor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proveedores.Proveedor'])),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal(u'proveedores', ['Telefono'])


    def backwards(self, orm):
        # Deleting model 'Proveedor'
        db.delete_table(u'proveedores_proveedor')

        # Deleting model 'Telefono'
        db.delete_table(u'proveedores_telefono')


    models = {
        u'proveedores.proveedor': {
            'Meta': {'object_name': 'Proveedor'},
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'proveedores.telefono': {
            'Meta': {'object_name': 'Telefono'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proveedor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['proveedores.Proveedor']"}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['proveedores']