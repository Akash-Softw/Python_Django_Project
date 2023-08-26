# Generated by Django 4.1.2 on 2023-08-26 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloapp', '0004_member_age_member_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='occupation',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
