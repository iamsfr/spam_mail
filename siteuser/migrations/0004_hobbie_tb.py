# Generated by Django 4.1 on 2022-09-17 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0009_rename_hobbie_tb_hobbiename_tb'),
        ('siteuser', '0003_register_tb_answer_register_tb_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='hobbie_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobbieid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteadmin.hobbiename_tb')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteuser.register_tb')),
            ],
        ),
    ]
