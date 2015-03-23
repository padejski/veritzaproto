# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Company', fields ['system_id']
        db.delete_unique(u'core_company', ['system_id'])

        # Adding model 'ElectionsContributionCompany'
        db.create_table(u'core_electionscontributioncompany', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.User'], null=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_ok', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Company'])),
            ('election_contribution', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ElectionsContributions'])),
        ))
        db.send_create_signal(u'core', ['ElectionsContributionCompany'])


    def backwards(self, orm):
        # Deleting model 'ElectionsContributionCompany'
        db.delete_table(u'core_electionscontributioncompany')

        # Adding unique constraint on 'Company', fields ['system_id']
        db.create_unique(u'core_company', ['system_id'])


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
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Company']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_ok': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'procurement': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.PublicProcurement']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        },
        u'core.company': {
            'Meta': {'object_name': 'Company'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'activity': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.User']", 'null': 'True'}),
            'economic_activity': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identification_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'is_ok': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'mail_address': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'registration_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'registration_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'system_id': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        },
        u'core.companymember': {
            'Meta': {'object_name': 'CompanyMember'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Company']", 'null': 'True'}),
            'company_registration_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.User']", 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_ok': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        },
        u'core.companymembertitle': {
            'Meta': {'object_name': 'CompanyMemberTitle'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'company_member': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.CompanyMember']", 'null': 'True'}),
            'company_registration_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'company_share': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_ok': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        },
        u'core.conflictinterest': {
            'Meta': {'object_name': 'ConflictInterest'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Company']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'official': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.PublicOfficial']"}),
            'public_procurement': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.PublicProcurement']"})
        },
        u'core.conflictinterestfamilymember': {
            'Meta': {'object_name': 'ConflictInterestFamilyMember'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Company']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.FamilyMember']"}),
            'public_procurement': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.PublicProcurement']"})
        },
        u'core.contractingauthority': {
            'Meta': {'object_name': 'ContractingAuthority'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.User']", 'null': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identification_number': ('django.db.models.fields.CharField', [], {'max_length': '40', 'db_index': 'True'}),
            'is_ok': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'procurement_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'procurement_system_id': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'town': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'webpage': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'})
        },
        u'core.contributorcompanyprocurement': {
            'Meta': {'object_name': 'ContributorCompanyProcurement'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Company']"}),
            'contribution_record': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.ElectionsContributions']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_ok': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'procurement': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.PublicProcurement']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        },
        u'core.contributorindividualprocurement': {
            'Meta': {'object_name': 'ContributorIndividualProcurement'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Company']"}),
            'contribution_record': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.ElectionsContributions']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'individual': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.CompanyMember']"}),
            'is_ok': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'procurement': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.PublicProcurement']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        },
        u'core.dataset': {
            'Meta': {'object_name': 'Dataset'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.User']", 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_ok': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['core.Tag']", 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        },
        u'core.electionscontributioncompany': {
            'Meta': {'object_name': 'ElectionsContributionCompany'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Company']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.User']", 'null': 'True'}),
            'election_contribution': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.ElectionsContributions']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_ok': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        },
        u'core.electionscontributions': {
            'Meta': {'object_name': 'ElectionsContributions'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'candidate': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'contributor_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'contributor_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'contributor_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.User']", 'null': 'True'}),
            'csv_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'election_place': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'election_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_ok': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'political_party': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        },
        u'core.familymember': {
            'Meta': {'object_name': 'FamilyMember'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_ok': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'public_official': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.PublicOfficial']"}),
            'relationship': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        },
        u'core.familymembercompany': {
            'Meta': {'object_name': 'FamilyMemberCompany'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Company']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_ok': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.FamilyMember']"}),
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
            'is_ok': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'middle_names': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'national_id': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'national_id_type': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        },
        u'core.procurementcompany': {
            'Meta': {'object_name': 'ProcurementCompany'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'contact_point': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.User']", 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identification_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'is_ok': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'postal_address': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'procurement_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'procurement_system_id': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'town': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'webpage': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        u'core.procurementcompanyraw': {
            'Meta': {'object_name': 'ProcurementCompanyRaw'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'contact_point': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.User']", 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identification_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'is_ok': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'postal_address': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'procurement_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'procurement_system_id': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'town': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'webpage': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        u'core.publicofficial': {
            'Meta': {'object_name': 'PublicOfficial'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_ok': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'system_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        },
        u'core.publicofficialcompany': {
            'Meta': {'object_name': 'PublicOfficialCompany'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Company']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'official': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.PublicOfficial']"})
        },
        u'core.publicofficialreport': {
            'Meta': {'object_name': 'PublicOfficialReport'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'annual_income': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'companies': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'company_board_member': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'company_salary': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.User']", 'null': 'True'}),
            'credits_debts': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_ok': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'job': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'movables': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'movables_others': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'official': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.PublicOfficial']", 'null': 'True'}),
            'official_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'other_activities': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'other_activities_salary': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'other_income': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'public_office': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'public_office_other': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'rbr': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'real_estate': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'report_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'report_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'salary': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'spouse': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'spouse_annual_income': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'spouse_companies': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'spouse_company_salary': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'spouse_credits_debts': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'spouse_job': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'spouse_movables': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'spouse_movables_others': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'spouse_other_activities': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'spouse_other_income': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'spouse_real_estate': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'system_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'})
        },
        u'core.publicprocurement': {
            'Meta': {'object_name': 'PublicProcurement'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.User']", 'null': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_ok': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'record_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'system_id': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'value': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'})
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
            'is_ok': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sources': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Dataset']", 'symmetrical': 'False'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        }
    }

    complete_apps = ['core']
