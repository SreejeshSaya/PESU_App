# Generated by Django 3.1.7 on 2021-04-06 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0006_auto_20210406_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='regNo',
            field=models.CharField(default='PESTECH000', max_length=10, primary_key=True, serialize=False, verbose_name='Reg No'),
        ),
    ]
