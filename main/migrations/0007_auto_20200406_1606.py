# Generated by Django 2.2.12 on 2020-04-06 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_donations_orderid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donations',
            name='done',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='donations',
            name='txnid',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='donations',
            name='txnstatus',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
