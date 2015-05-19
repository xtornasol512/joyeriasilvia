# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Libreta'
        db.create_table(u'clientes_libreta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('notas', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'clientes', ['Libreta'])

        # Adding M2M table for field cliente on 'Libreta'
        m2m_table_name = db.shorten_name(u'clientes_libreta_cliente')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('libreta', models.ForeignKey(orm[u'clientes.libreta'], null=False)),
            ('cliente', models.ForeignKey(orm[u'clientes.cliente'], null=False))
        ))
        db.create_unique(m2m_table_name, ['libreta_id', 'cliente_id'])

        # Adding model 'TipoTelefono'
        db.create_table(u'clientes_tipotelefono', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'clientes', ['TipoTelefono'])

        # Deleting field 'Telefono.nombre'
        db.delete_column(u'clientes_telefono', 'nombre')

        # Adding field 'Telefono.tipo'
        db.add_column(u'clientes_telefono', 'tipo',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.TipoTelefono'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Libreta'
        db.delete_table(u'clientes_libreta')

        # Removing M2M table for field cliente on 'Libreta'
        db.delete_table(db.shorten_name(u'clientes_libreta_cliente'))

        # Deleting model 'TipoTelefono'
        db.delete_table(u'clientes_tipotelefono')

        # Adding field 'Telefono.nombre'
        db.add_column(u'clientes_telefono', 'nombre',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Telefono.tipo'
        db.delete_column(u'clientes_telefono', 'tipo_id')


    models = {
        u'clientes.cliente': {
            'Meta': {'object_name': 'Cliente'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notas': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'clientes.libreta': {
            'Meta': {'object_name': 'Libreta'},
            'cliente': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['clientes.Cliente']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'notas': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'clientes.telefono': {
            'Meta': {'object_name': 'Telefono'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Cliente']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.TipoTelefono']", 'null': 'True', 'blank': 'True'})
        },
        u'clientes.tipotelefono': {
            'Meta': {'object_name': 'TipoTelefono'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['clientes']