# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Payment'
        db.create_table(u'yandex_money_payment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('custome_number', self.gf('django.db.models.fields.CharField')(default='df186d226a5144d6bc0c99b07ee9be64', unique=True, max_length=64)),
            ('status', self.gf('django.db.models.fields.CharField')(default='processed', max_length=16)),
            ('scid', self.gf('django.db.models.fields.PositiveIntegerField')(default=51557)),
            ('shop_id', self.gf('django.db.models.fields.PositiveIntegerField')(default=15522)),
            ('payment_type', self.gf('django.db.models.fields.CharField')(default='pc', max_length=2)),
            ('invoice_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('order_amount', self.gf('django.db.models.fields.FloatField')()),
            ('shop_amount', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('order_currency', self.gf('django.db.models.fields.PositiveIntegerField')(default=643)),
            ('shop_currency', self.gf('django.db.models.fields.PositiveIntegerField')(default=643, null=True, blank=True)),
            ('payer_code', self.gf('django.db.models.fields.CharField')(max_length=33, null=True, blank=True)),
            ('success_url', self.gf('django.db.models.fields.URLField')(default='http://example.com/success-payment/', max_length=200)),
            ('fail_url', self.gf('django.db.models.fields.URLField')(default='http://example.com/fail-payment/', max_length=200)),
            ('cps_email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('cps_phone', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('performed_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'yandex_money', ['Payment'])


    def backwards(self, orm):
        # Deleting model 'Payment'
        db.delete_table(u'yandex_money_payment')


    models = {
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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'yandex_money.payment': {
            'Meta': {'ordering': "('pub_date',)", 'object_name': 'Payment'},
            'cps_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'cps_phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'custome_number': ('django.db.models.fields.CharField', [], {'default': "'2f86f57bac4442779fc9642907b53c3e'", 'unique': 'True', 'max_length': '64'}),
            'fail_url': ('django.db.models.fields.URLField', [], {'default': "'http://example.com/fail-payment/'", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'order_amount': ('django.db.models.fields.FloatField', [], {}),
            'order_currency': ('django.db.models.fields.PositiveIntegerField', [], {'default': '643'}),
            'payer_code': ('django.db.models.fields.CharField', [], {'max_length': '33', 'null': 'True', 'blank': 'True'}),
            'payment_type': ('django.db.models.fields.CharField', [], {'default': "'pc'", 'max_length': '2'}),
            'performed_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'scid': ('django.db.models.fields.PositiveIntegerField', [], {'default': '51557'}),
            'shop_amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'shop_currency': ('django.db.models.fields.PositiveIntegerField', [], {'default': '643', 'null': 'True', 'blank': 'True'}),
            'shop_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '15522'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'processed'", 'max_length': '16'}),
            'success_url': ('django.db.models.fields.URLField', [], {'default': "'http://example.com/success-payment/'", 'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['yandex_money']