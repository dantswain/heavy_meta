# Generated by Django 2.0.1 on 2018-01-21 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hm_web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='take',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]