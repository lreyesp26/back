# Generated by Django 5.0 on 2023-12-23 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('crazon_social', models.CharField(blank=True, max_length=300, null=True)),
                ('ctelefono', models.CharField(max_length=300)),
                ('tipocliente', models.CharField(choices=[('04', '04'), ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08')], max_length=2, null=True)),
                ('cregistro', models.DateTimeField(auto_now_add=True)),
                ('snombre', models.CharField(blank=True, max_length=300, null=True)),
                ('capellido', models.CharField(blank=True, max_length=300, null=True)),
                ('cpuntos', models.DecimalField(decimal_places=0, default=0, max_digits=3)),
                ('id_ubicacion1', models.IntegerField(blank=True, null=True)),
                ('id_ubicacion2', models.IntegerField(blank=True, null=True)),
                ('id_ubicacion3', models.IntegerField(blank=True, null=True)),
                ('ruc_cedula', models.CharField(blank=True, max_length=300, null=True)),
                ('ccorreo_electronico', models.CharField(blank=True, max_length=300, null=True)),
                ('ubicacion', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'db_table': 'clientes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ubicaciones',
            fields=[
                ('id_ubicacion', models.AutoField(primary_key=True, serialize=False)),
                ('latitud', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitud', models.DecimalField(decimal_places=6, max_digits=9)),
                ('udescripcion', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'ubicaciones',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Combo',
        ),
    ]
