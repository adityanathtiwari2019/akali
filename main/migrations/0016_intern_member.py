# Generated by Django 2.2.12 on 2020-04-07 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_sitesocial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('duration', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('age', models.PositiveIntegerField()),
                ('state', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('city', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('college', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('course', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('interest', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('laptop', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('startdate', models.DateField(default=None)),
                ('applydate', models.DateTimeField(auto_now_add=True)),
                ('resume', models.FileField(blank=True, upload_to='resumes/%Y/%m/%d')),
            ],
            options={
                'ordering': ('applydate',),
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('dob', models.DateField(blank=True, default=None, null=True)),
                ('gender', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('state', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('city', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('address', models.CharField(blank=True, default=None, max_length=500, null=True)),
                ('pincode', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('voterid', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('joindate', models.DateTimeField(auto_now_add=True)),
                ('volunteer', models.BooleanField(default=False)),
                ('contribute', models.CharField(blank=True, default=None, max_length=500, null=True)),
                ('aboutself', models.TextField(blank=True, default=None, null=True)),
            ],
            options={
                'ordering': ('joindate',),
            },
        ),
    ]
