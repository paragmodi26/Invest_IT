# Generated by Django 3.0.4 on 2021-01-12 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210110_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='refer_code',
            field=models.CharField(default='NULL', max_length=100),
        ),
    ]
