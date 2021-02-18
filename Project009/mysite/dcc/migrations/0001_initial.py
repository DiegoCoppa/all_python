# Generated by Django 3.1.4 on 2021-02-17 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DccDepts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcc_dept', models.CharField(default='', max_length=20)),
                ('dcc_centro', models.CharField(default='', max_length=20)),
                ('dcc_PermisosDept', models.IntegerField(default=0)),
                ('dcc_CentroDeCosto', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DccUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcc_user', models.CharField(default='', max_length=10)),
                ('dcc_pass_full', models.CharField(default='', max_length=8)),
                ('dcc_nombre_full', models.CharField(default='', max_length=150)),
                ('dcc_permisosuser', models.IntegerField(default=0)),
                ('dcc_Email', models.CharField(default='', max_length=150)),
                ('dcc_belong_Dept', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dcc.dccdepts')),
            ],
        ),
        migrations.CreateModel(
            name='DccProcs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcc_proc_nombre', models.CharField(default='', max_length=20)),
                ('dcc_root_folder', models.CharField(default='', max_length=150)),
                ('dcc_dept_manager', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dcc.dccdepts')),
            ],
        ),
        migrations.CreateModel(
            name='DccCerts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(default='', max_length=10)),
                ('dcc_numero_certificado', models.IntegerField(default=0)),
                ('dcc_numero_parcial', models.IntegerField(default=0)),
                ('dcc_root_folder', models.CharField(default='', max_length=150)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('dcc_proc', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dcc.dccprocs')),
                ('dcc_user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dcc.dccusers')),
            ],
        ),
    ]
