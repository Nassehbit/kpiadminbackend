# Generated by Django 3.2 on 2021-04-27 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_clientinformation_joindate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientinformation',
            name='phone',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
