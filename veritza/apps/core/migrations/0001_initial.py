# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'core_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
        ))
        db.send_create_signal(u'core', ['User'])

        # Adding M2M table for field groups on 'User'
        m2m_table_name = db.shorten_name(u'core_user_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'core.user'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'User'
        m2m_table_name = db.shorten_name(u'core_user_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'core.user'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'permission_id'])

        # Adding M2M table for field subscriptions on 'User'
        m2m_table_name = db.shorten_name(u'core_user_subscriptions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'core.user'], null=False)),
            ('veritza', models.ForeignKey(orm[u'core.veritza'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'veritza_id'])

        # Adding model 'UserProfile'
        db.create_table(u'core_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mugshot', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('privacy', self.gf('django.db.models.fields.CharField')(default='registered', max_length=15)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='profile', unique=True, to=orm['core.User'])),
        ))
        db.send_create_signal(u'core', ['UserProfile'])

        # Adding model 'Person'
        db.create_table(u'core_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.User'], null=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('national_id', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('national_id_type', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('middle_names', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('birth_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Person'])

        # Adding model 'Dataset'
        db.create_table(u'core_dataset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.User'], null=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Dataset'])

        # Adding M2M table for field tags on 'Dataset'
        m2m_table_name = db.shorten_name(u'core_dataset_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dataset', models.ForeignKey(orm[u'core.dataset'], null=False)),
            ('tag', models.ForeignKey(orm[u'core.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['dataset_id', 'tag_id'])

        # Adding model 'Veritza'
        db.create_table(u'core_veritza', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.User'], null=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Veritza'])

        # Adding M2M table for field sources on 'Veritza'
        m2m_table_name = db.shorten_name(u'core_veritza_sources')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('veritza', models.ForeignKey(orm[u'core.veritza'], null=False)),
            ('dataset', models.ForeignKey(orm[u'core.dataset'], null=False))
        ))
        db.create_unique(m2m_table_name, ['veritza_id', 'dataset_id'])

        # Adding model 'PublicOfficialReport'
        db.create_table(u'core_publicofficialreport', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.User'], null=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('system_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('public_office', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('public_office_other', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('official_type', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('job', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('salary', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('movables', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('real_estate', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('companies', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('report_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('report_type', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=10, null=True)),
            ('rbr', self.gf('django.db.models.fields.CharField')(max_length=10, null=True)),
            ('spouse_job', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('spouse_salary', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('spouse_companies', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('spouse_movables', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('spouse_real_estate', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
        ))
        db.send_create_signal(u'core', ['PublicOfficialReport'])

        # Adding model 'Company'
        db.create_table(u'core_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.User'], null=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('registration_number', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('identification_number', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('mail_address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=32, null=True)),
            ('registration_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('activity', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('economic_activity', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
        ))
        db.send_create_signal(u'core', ['Company'])

        # Adding model 'BidderCompany'
        db.create_table(u'core_biddercompany', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.User'], null=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('identification_number', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('town', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True)),
            ('postal_address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('webpage', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('contact_point', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
        ))
        db.send_create_signal(u'core', ['BidderCompany'])

        # Adding model 'ContractingAuthority'
        db.create_table(u'core_contractingauthority', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.User'], null=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('identification_number', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('town', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('webpage', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
        ))
        db.send_create_signal(u'core', ['ContractingAuthority'])

        # Adding model 'PublicProcurement'
        db.create_table(u'core_publicprocurement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.User'], null=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True)),
            ('record_type', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('bidder', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.BidderCompany'], null=True)),
            ('authority', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ContractingAuthority'], null=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['PublicProcurement'])

        # Adding model 'ConflictInterest'
        db.create_table(u'core_conflictinterest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('official', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.PublicOfficialReport'])),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Company'])),
            ('public_procurement', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.PublicProcurement'])),
        ))
        db.send_create_signal(u'core', ['ConflictInterest'])

        # Adding model 'UserSettings'
        db.create_table(u'core_usersettings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.User'], unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'core', ['UserSettings'])

        # Adding model 'Alert'
        db.create_table(u'core_alert', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.User'])),
            ('veritza', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Veritza'], null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Alert'])

        # Adding model 'Tag'
        db.create_table(u'core_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'core', ['Tag'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'core_user')

        # Removing M2M table for field groups on 'User'
        db.delete_table(db.shorten_name(u'core_user_groups'))

        # Removing M2M table for field user_permissions on 'User'
        db.delete_table(db.shorten_name(u'core_user_user_permissions'))

        # Removing M2M table for field subscriptions on 'User'
        db.delete_table(db.shorten_name(u'core_user_subscriptions'))

        # Deleting model 'UserProfile'
        db.delete_table(u'core_userprofile')

        # Deleting model 'Person'
        db.delete_table(u'core_person')

        # Deleting model 'Dataset'
        db.delete_table(u'core_dataset')

        # Removing M2M table for field tags on 'Dataset'
        db.delete_table(db.shorten_name(u'core_dataset_tags'))

        # Deleting model 'Veritza'
        db.delete_table(u'core_veritza')

        # Removing M2M table for field sources on 'Veritza'
        db.delete_table(db.shorten_name(u'core_veritza_sources'))

        # Deleting model 'PublicOfficialReport'
        db.delete_table(u'core_publicofficialreport')

        # Deleting model 'Company'
        db.delete_table(u'core_company')

        # Deleting model 'BidderCompany'
        db.delete_table(u'core_biddercompany')

        # Deleting model 'ContractingAuthority'
        db.delete_table(u'core_contractingauthority')

        # Deleting model 'PublicProcurement'
        db.delete_table(u'core_publicprocurement')

        # Deleting model 'ConflictInterest'
        db.delete_table(u'core_conflictinterest')

        # Deleting model 'UserSettings'
        db.delete_table(u'core_usersettings')

        # Deleting model 'Alert'
        db.delete_table(u'core_alert')

        # Deleting model 'Tag'
        db.delete_table(u'core_tag')


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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.alert': {
            'Meta': {'object_name': 'Alert'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.User']"}),
            'veritza': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Veritza']", 'null': 'True', 'blank': 'True'})
        },
        u'core.biddercompany': {
            'Meta': {'object_name': 'BidderCompany'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'contact_point': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.User']", 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identification_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'postal_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'town': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'webpage': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        u'core.company': {
            'Meta': {'object_name': 'Company'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'activity': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.User']", 'null': 'True'}),
            'economic_activity': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identification_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'mail_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'registration_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'registration_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        },
        u'core.conflictinterest': {
            'Meta': {'object_name': 'ConflictInterest'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Company']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'official': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.PublicOfficialReport']"}),
            'public_procurement': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.PublicProcurement']"})
        },
        u'core.contractingauthority': {
            'Meta': {'object_name': 'ContractingAuthority'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.User']", 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identification_number': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'town': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'webpage': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'})
        },
        u'core.dataset': {
            'Meta': {'object_name': 'Dataset'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.User']", 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['core.Tag']", 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        },
        u'core.person': {
            'Meta': {'object_name': 'Person'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'birth_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.User']", 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'middle_names': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'national_id': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'national_id_type': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        },
        u'core.publicofficialreport': {
            'Meta': {'object_name': 'PublicOfficialReport'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'companies': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'movables': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'official_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'public_office': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'public_office_other': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'rbr': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'real_estate': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'report_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'report_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'salary': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'spouse_companies': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'spouse_job': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'spouse_movables': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'spouse_real_estate': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'spouse_salary': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'system_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'})
        },
        u'core.publicprocurement': {
            'Meta': {'object_name': 'PublicProcurement'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'authority': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.ContractingAuthority']", 'null': 'True'}),
            'bidder': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.BidderCompany']", 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.User']", 'null': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_number': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'record_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        },
        u'core.tag': {
            'Meta': {'object_name': 'Tag'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'core.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'subscriptions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Veritza']", 'symmetrical': 'False'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        },
        u'core.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mugshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'privacy': ('django.db.models.fields.CharField', [], {'default': "'registered'", 'max_length': '15'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'profile'", 'unique': 'True', 'to': u"orm['core.User']"})
        },
        u'core.usersettings': {
            'Meta': {'object_name': 'UserSettings'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.User']", 'unique': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'core.veritza': {
            'Meta': {'object_name': 'Veritza'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.User']", 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sources': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Dataset']", 'symmetrical': 'False'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        }
    }

    complete_apps = ['core']