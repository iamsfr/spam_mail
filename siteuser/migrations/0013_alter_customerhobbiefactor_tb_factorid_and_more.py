# Generated by Django 4.1 on 2022-09-29 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0014_age_tb'),
        ('siteuser', '0012_customerhobbiefactor_tb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerhobbiefactor_tb',
            name='factorid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteadmin.hobbiefactor_tb'),
        ),
        migrations.AlterField(
            model_name='customerhobbiefactor_tb',
            name='hobbieid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteadmin.hobbiename_tb'),
        ),
        migrations.AlterField(
            model_name='customerhobbiefactor_tb',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteuser.register_tb'),
        ),
    ]