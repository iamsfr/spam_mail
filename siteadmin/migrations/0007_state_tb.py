# Generated by Django 4.1 on 2022-09-17 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0006_delete_state_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='state_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=50)),
                ('countryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteadmin.country_tb')),
            ],
        ),
    ]
