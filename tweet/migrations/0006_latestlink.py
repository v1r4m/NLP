# Generated by Django 4.1.1 on 2022-09-30 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0005_remove_post_pklink'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=19)),
            ],
        ),
    ]