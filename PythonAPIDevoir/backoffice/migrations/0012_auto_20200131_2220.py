# Generated by Django 3.0.2 on 2020-01-31 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0011_remove_subject_idsubject'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='HEIGHT',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='WEIGHT',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
