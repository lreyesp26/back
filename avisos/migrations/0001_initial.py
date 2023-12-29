# Generated by Django 5.0 on 2023-12-28 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvisosPrincipales',
            fields=[
                ('id_aviso', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=150)),
                ('descripcion', models.CharField(blank=True, max_length=500, null=True)),
                ('imagen', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'avisosprincipales',
                'managed': False,
            },
        ),
    ]