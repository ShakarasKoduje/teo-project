# Generated by Django 2.2.1 on 2019-05-25 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teoapp', '0015_auto_20190521_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='postauthor',
            name='nameId',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='postauthor',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
