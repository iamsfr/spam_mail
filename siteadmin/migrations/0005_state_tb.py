# Generated by Django 4.1 on 2022-09-17 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0004_country_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='state_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=50)),
            ],
        ),
    ]
