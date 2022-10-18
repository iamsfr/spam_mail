# Generated by Django 4.1 on 2022-09-29 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0014_age_tb'),
        ('siteuser', '0011_rename_blacklist_blacklist_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='customerhobbiefactor_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factorid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hobbiefactor', to='siteadmin.hobbiefactor_tb')),
                ('hobbieid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hobbieid', to='siteadmin.hobbiename_tb')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userid2', to='siteuser.register_tb')),
            ],
        ),
    ]
