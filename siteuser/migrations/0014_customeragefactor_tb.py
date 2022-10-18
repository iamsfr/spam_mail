# Generated by Django 4.1 on 2022-09-29 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0014_age_tb'),
        ('siteuser', '0013_alter_customerhobbiefactor_tb_factorid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='customeragefactor_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factorid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteadmin.age_tb')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteuser.register_tb')),
            ],
        ),
    ]
