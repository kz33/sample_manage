# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-24 02:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sm_main', '0002_auto_20180223_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='doc_file_path',
            field=models.FileField(help_text='上传的文档', null=True, upload_to='sample_manage/doc_file/', verbose_name='上传的文档'),
        ),
    ]