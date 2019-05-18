# Generated by Django 2.2.1 on 2019-05-18 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teoapp', '0003_auto_20190518_0907'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='PostContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('author', models.ManyToManyField(to='teoapp.PostAuthor')),
            ],
        ),
    ]