# Generated by Django 2.2.1 on 2019-05-18 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teoapp', '0009_postcontent__content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcontent',
            name='_content',
            field=models.TextField(),
        ),
    ]
