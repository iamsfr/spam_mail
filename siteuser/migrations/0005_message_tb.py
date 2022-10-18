# Generated by Django 4.1 on 2022-09-21 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteuser', '0004_hobbie_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='message_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('status', models.CharField(default='pending', max_length=50)),
                ('filterstatus', models.CharField(default='pending', max_length=50)),
                ('receiverid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='siteuser.register_tb')),
                ('senderid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='siteuser.register_tb')),
            ],
        ),
    ]