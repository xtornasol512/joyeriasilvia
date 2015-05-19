# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Venta'
        db.create_table(u'ventas_venta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Cliente'])),
            ('total', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('contado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fecha', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('notas', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'ventas', ['Venta'])

        # Adding model 'ListaJoya'
        db.create_table(u'ventas_listajoya', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('venta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ventas.Venta'])),
            ('joya', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['almacen.Joya'])),
        ))
        db.send_create_signal(u'ventas', ['ListaJoya'])

        # Adding model 'CarroTemporal'
        db.create_table(u'ventas_carrotemporal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('joya', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['almacen.Joya'])),
            ('venta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ventas.Venta'])),
        ))
        db.send_create_signal(u'ventas', ['CarroTemporal'])


    def backwards(self, orm):
        # Deleting model 'Venta'
        db.delete_table(u'ventas_venta')

        # Deleting model 'ListaJoya'
        db.delete_table(u'ventas_listajoya')

        # Deleting model 'CarroTemporal'
        db.delete_table(u'ventas_carrotemporal')


    models = {
        u'almacen.joya': {
            'Meta': {'object_name': 'Joya'},
            'costo': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'existente': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'fechaCompra': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'peso': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '3'}),
            'precioVentaContado': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'precioVentaPagos': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'proveedor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['proveedores.Proveedor']", 'null': 'True', 'blank': 'True'}),
            'tipoJoya': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['almacen.TipoJoya']"})
        },
        u'almacen.tipojoya': {
            'Meta': {'object_name': 'TipoJoya'},
            'clave': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '5'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'valor': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'clientes.cliente': {
            'Meta': {'object_name': 'Cliente'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notas': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'proveedores.proveedor': {
            'Meta': {'object_name': 'Proveedor'},
            'clave': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4'}),
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'ventas.carrotemporal': {
            'Meta': {'object_name': 'CarroTemporal'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'joya': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['almacen.Joya']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'venta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ventas.Venta']"})
        },
        u'ventas.listajoya': {
            'Meta': {'object_name': 'ListaJoya'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'joya': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['almacen.Joya']"}),
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

    complete_apps = ['ventas']