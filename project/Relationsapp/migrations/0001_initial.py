# Generated by Django 3.2.6 on 2021-08-14 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departmentbranch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Studentdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('marks', models.IntegerField(max_length=150)),
                ('dept', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Relationsapp.departmentbranch')),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('depbranch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Relationsapp.departmentbranch')),
            ],
        ),
    ]
