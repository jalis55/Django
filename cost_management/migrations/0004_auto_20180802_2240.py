# Generated by Django 2.0.6 on 2018-08-02 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cost_management', '0003_auto_20180708_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]