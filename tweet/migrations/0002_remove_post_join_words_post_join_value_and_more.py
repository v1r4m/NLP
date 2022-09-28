# Generated by Django 4.1.1 on 2022-09-28 09:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='join_words',
        ),
        migrations.AddField(
            model_name='post',
            name='join_value',
            field=models.IntegerField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='join_word',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='pkWord',
            field=models.CharField(max_length=10),
        ),
    ]
