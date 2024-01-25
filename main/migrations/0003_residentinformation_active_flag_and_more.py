# Generated by Django 4.2.5 on 2023-10-27 02:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_residentinformation_active_flag_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='residentinformation',
            name='active_flag',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='address',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='address_block',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='address_block_no',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='address_building',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='address_phase',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='address_street_no',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='address_subdivision',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='address_unit_no',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='arrival_status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='birth_attendant',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='blk_lot_phase',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='blood_type',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='citizenship',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='civil_status',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='contact_number',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='date_of_arrival',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='date_started_working',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='disability',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='disability_citizen_id_no',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='educational_attainment',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='email_address',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='employment_status',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='enrollment_status',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='ethnicity',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='from_what_country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='gsis_no',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='health_facility_visited_last_six_months',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='immunization',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='income_status',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='is_indigenous',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='is_mic_complete',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='is_ofw',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='is_rbi_complete',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='is_registered_senior_citizen',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='is_registered_voter',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='issued_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='lot_ownership',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='monthly_income',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='national_id',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='occupation',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='patient_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='persons_staying_in_the_household',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='place_of_birth',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='place_of_delivery',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='place_of_school',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='place_of_work',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='previous_residence',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='profile_picture',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='qualifier',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='reason_for_visit',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='relation_to_household_head',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='religion',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='school_type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='senior_citizen_id_no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='sex',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='skills_development_training',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='solo_parent',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='sss_no',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='tin_no',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='type_of_document',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='voting_precint',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='residentinformation',
            name='where_document_issued',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
