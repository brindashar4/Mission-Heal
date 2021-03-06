# Generated by Django 2.0.3 on 2018-04-01 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ngo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngo_name', models.CharField(max_length=250)),
                ('ngo_logo', models.CharField(max_length=500)),
                ('ngo_loc', models.CharField(max_length=500)),
                ('relief_type', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='NgoDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField(max_length=5000)),
                ('address', models.TextField(max_length=5000)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ngo.Ngo')),
            ],
        ),
    ]
