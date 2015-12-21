# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usa', '0028_auto_20150616_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fedcandidate',
            name='cand_city',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'City'),
        ),
        migrations.AlterField(
            model_name='fedcandidate',
            name='cand_election_yr',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Election Year'),
        ),
        migrations.AlterField(
            model_name='fedcandidate',
            name='cand_ici',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Incumbent Challenger Status'),
        ),
        migrations.AlterField(
            model_name='fedcandidate',
            name='cand_id',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedcandidate',
            name='cand_name',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Name'),
        ),
        migrations.AlterField(
            model_name='fedcandidate',
            name='cand_office',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Office'),
        ),
        migrations.AlterField(
            model_name='fedcandidate',
            name='cand_office_district',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'District'),
        ),
        migrations.AlterField(
            model_name='fedcandidate',
            name='cand_office_st',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Office State'),
        ),
        migrations.AlterField(
            model_name='fedcandidate',
            name='cand_pcc',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Campaign Committee'),
        ),
        migrations.AlterField(
            model_name='fedcandidate',
            name='cand_pty_affiliation',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Party Affiliation'),
        ),
        migrations.AlterField(
            model_name='fedcandidate',
            name='cand_st',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'State'),
        ),
        migrations.AlterField(
            model_name='fedcandidate',
            name='cand_st1',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Street'),
        ),
        migrations.AlterField(
            model_name='fedcandidate',
            name='cand_st2',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Street2'),
        ),
        migrations.AlterField(
            model_name='fedcandidate',
            name='cand_status',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Status'),
        ),
        migrations.AlterField(
            model_name='fedcandidate',
            name='cand_zip',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Zip Code'),
        ),
        migrations.AlterField(
            model_name='fedcandidate',
            name='url',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedcompany',
            name='place',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='fedcpscrecall',
            name='consumer_contact',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Consumer Contact'),
        ),
        migrations.AlterField(
            model_name='fedcpscrecall',
            name='desc',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedcpscrecall',
            name='hazards',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedcpscrecall',
            name='images',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedcpscrecall',
            name='in_conj',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedcpscrecall',
            name='injuries',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedcpscrecall',
            name='last_pub_date',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedcpscrecall',
            name='mfcs',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Manufacturers'),
        ),
        migrations.AlterField(
            model_name='fedcpscrecall',
            name='mfcs_countries',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedcpscrecall',
            name='product_upcs',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedcpscrecall',
            name='products',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedcpscrecall',
            name='recall_date',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedcpscrecall',
            name='recall_id',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedcpscrecall',
            name='recall_num',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedcpscrecall',
            name='remedies',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedcpscrecall',
            name='retailers',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedcpscrecall',
            name='title',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedcpscrecall',
            name='url',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedcpscrecallviolation',
            name='action_requested',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Action Requested'),
        ),
        migrations.AlterField(
            model_name='fedcpscrecallviolation',
            name='address_1',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Address'),
        ),
        migrations.AlterField(
            model_name='fedcpscrecallviolation',
            name='address_2',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedcpscrecallviolation',
            name='citation',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedcpscrecallviolation',
            name='country',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedcpscrecallviolation',
            name='firm',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedcpscrecallviolation',
            name='foreign_mfg',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Foreign Manufacturing'),
        ),
        migrations.AlterField(
            model_name='fedcpscrecallviolation',
            name='loa_date',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'LOA Date'),
        ),
        migrations.AlterField(
            model_name='fedcpscrecallviolation',
            name='lot_size',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Lot Size'),
        ),
        migrations.AlterField(
            model_name='fedcpscrecallviolation',
            name='model',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedcpscrecallviolation',
            name='primary_violation',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Primary Violation'),
        ),
        migrations.AlterField(
            model_name='fedcpscrecallviolation',
            name='product',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedcpscrecallviolation',
            name='url',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedelectioncontribution',
            name='amndt_ind',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Amendment'),
        ),
        migrations.AlterField(
            model_name='fedelectioncontribution',
            name='cand_id',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Candidate'),
        ),
        migrations.AlterField(
            model_name='fedelectioncontribution',
            name='city',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedelectioncontribution',
            name='cmte_id',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Committee ID'),
        ),
        migrations.AlterField(
            model_name='fedelectioncontribution',
            name='employer',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedelectioncontribution',
            name='entity_tp',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Entity Type'),
        ),
        migrations.AlterField(
            model_name='fedelectioncontribution',
            name='file_num',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'File Number'),
        ),
        migrations.AlterField(
            model_name='fedelectioncontribution',
            name='image_num',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Microfilm Location'),
        ),
        migrations.AlterField(
            model_name='fedelectioncontribution',
            name='memo_cd',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Memo Code'),
        ),
        migrations.AlterField(
            model_name='fedelectioncontribution',
            name='memo_text',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Memo Text'),
        ),
        migrations.AlterField(
            model_name='fedelectioncontribution',
            name='name',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Contributor Name'),
        ),
        migrations.AlterField(
            model_name='fedelectioncontribution',
            name='occupation',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedelectioncontribution',
            name='other_id',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Other ID'),
        ),
        migrations.AlterField(
            model_name='fedelectioncontribution',
            name='rpt_tp',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Report Type'),
        ),
        migrations.AlterField(
            model_name='fedelectioncontribution',
            name='state',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedelectioncontribution',
            name='sub_id',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'FEC Record Number'),
        ),
        migrations.AlterField(
            model_name='fedelectioncontribution',
            name='tran_id',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Transaction ID'),
        ),
        migrations.AlterField(
            model_name='fedelectioncontribution',
            name='transaction_amt',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Transaction Amount'),
        ),
        migrations.AlterField(
            model_name='fedelectioncontribution',
            name='transaction_dt',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Transaction Date'),
        ),
        migrations.AlterField(
            model_name='fedelectioncontribution',
            name='transaction_pgi',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Primary-Gen Indicator'),
        ),
        migrations.AlterField(
            model_name='fedelectioncontribution',
            name='transaction_tp',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Transaction Type'),
        ),
        migrations.AlterField(
            model_name='fedelectioncontribution',
            name='url',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedelectioncontribution',
            name='zip_code',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Zip Code'),
        ),
        migrations.AlterField(
            model_name='fedfinancialdisclosure',
            name='filing',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='fedfinancialdisclosure',
            name='name',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='fedfinancialdisclosure',
            name='office',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='fedfinancialdisclosure',
            name='pdf',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='fedfinancialdisclosure',
            name='url',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedfinancialdisclosure',
            name='year',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='fedirsexemptorg',
            name='city',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedirsexemptorg',
            name='country',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedirsexemptorg',
            name='ein',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'EIN'),
        ),
        migrations.AlterField(
            model_name='fedirsexemptorg',
            name='name',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Legal Name'),
        ),
        migrations.AlterField(
            model_name='fedirsexemptorg',
            name='state',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedirsexemptorg',
            name='status',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Deductibility Status'),
        ),
        migrations.AlterField(
            model_name='fedirsexemptorg',
            name='url',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedoshaebsa',
            name='case_type',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Case Type'),
        ),
        migrations.AlterField(
            model_name='fedoshaebsa',
            name='ein',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'EIN'),
        ),
        migrations.AlterField(
            model_name='fedoshaebsa',
            name='final_close_date',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Closing Date'),
        ),
        migrations.AlterField(
            model_name='fedoshaebsa',
            name='final_close_reason',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Closing Reason'),
        ),
        migrations.AlterField(
            model_name='fedoshaebsa',
            name='penalty_amount',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Penalty Amount'),
        ),
        migrations.AlterField(
            model_name='fedoshaebsa',
            name='plan_admin',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Administrator'),
        ),
        migrations.AlterField(
            model_name='fedoshaebsa',
            name='plan_admin_state',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Admin State'),
        ),
        migrations.AlterField(
            model_name='fedoshaebsa',
            name='plan_admin_zip_code',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Admin Zip Code'),
        ),
        migrations.AlterField(
            model_name='fedoshaebsa',
            name='plan_name',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Plan Name'),
        ),
        migrations.AlterField(
            model_name='fedoshaebsa',
            name='plan_year',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Plan Year'),
        ),
        migrations.AlterField(
            model_name='fedoshaebsa',
            name='pn',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Plan Number'),
        ),
        migrations.AlterField(
            model_name='fedoshaebsa',
            name='url',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='activity_nr',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Inspection ID'),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='adv_notice',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Advance Notice'),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='case_mod_date',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='close_case_date',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='close_conf_date',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='estab_name',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Establishment Name'),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='health_const',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='health_manuf',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='health_marit',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='host_est_key',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='indstry_dim_id',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='insp_scope',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='insp_type',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='ld_dt',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='mail_city',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='mail_state',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='mail_street',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='mail_zip',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='migrant',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='naics_code',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'NAICS Code'),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='nr_in_estab',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='open_date',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='owner_code',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Owner Code'),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='owner_type',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='reporting_id',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='safety_const',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='safety_hlth',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='safety_manuf',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='safety_marit',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='sic_code',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='site_address',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='site_city',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'City'),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='site_state',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'State'),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='site_zip',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'ZIP'),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='state_flag',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='union_status',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='url',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='why_no_insp',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'No Inspection Reason'),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='zip_dim_id',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='accession_number',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='business_address',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='business_phone',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='central_index_key',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='city',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='company_conformed_name',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='company_data',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='conformed_submission_type',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='date_as_of_change',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='date_of_name_change',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='filed_as_of_date',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='filer',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='filing_values',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='film_number',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='fiscal_year_end',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='form_type',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='former_company',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='former_conformed_name',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='irs_number',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='mail_address',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='public_document_count',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='sec_act',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='sec_file_number',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='standard_industrial_classification',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='state',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='state_of_incorporation',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='street_1',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='street_2',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='url',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='zip',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='accuracy_value',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='census_block_code',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='city_name',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'City'),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='collect_desc',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='congressional_dist_num',
            field=models.CharField(max_length=1024, null=True, verbose_name=b''),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='conveyor',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='country_name',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Country'),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='county_name',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'County'),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='create_date',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Creation Date'),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='epa_region_code',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'EPA Region Code'),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='federal_agency_name',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Agency'),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='federal_facility_code',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Facility Code'),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='fips_code',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'FIPS Code'),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='frs_facility_detail_report_url',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Report URL'),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='hdatum_desc',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='huc_code',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'HUC Code'),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='interest_types',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='latitude83',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='location_address',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Location'),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='location_description',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='longitude83',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='naics_code_descriptions',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='naics_codes',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='pgm_sys_acrnms',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='postal_code',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='primary_name',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Primary Name'),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='ref_point_desc',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='registry_id',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Registry ID'),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='sic_code_descriptions',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='sic_codes',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='site_type_name',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='source_desc',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='state_code',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='state_name',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'State'),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='supplemental_location',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='tribal_land_code',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='tribal_land_name',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Tribal Land Name'),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='update_date',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Update Date'),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='url',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fedtoxicsfacility',
            name='us_mexico_border_ind',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]
