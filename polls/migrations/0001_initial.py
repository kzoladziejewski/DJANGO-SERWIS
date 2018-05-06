# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-01 18:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number_Of_Answer', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Name_of_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_of_Add', models.DateTimeField(default=django.utils.timezone.now)),
                ('Text_of_Question', models.CharField(default=None, max_length=255)),
                ('Image_of_Question', models.ImageField(default=None, upload_to=b'')),
                ('Correct_Answer', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Name_of_quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Grand', models.CharField(max_length=200)),
                ('Date_of_public', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(default='RADOM', max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='name_of_question',
            name='Membership_of_Question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Name_of_quiz'),
        ),
        migrations.AddField(
            model_name='answer',
            name='Text_of_Answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Name_of_Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='Who_Answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.User'),
        ),
    ]
