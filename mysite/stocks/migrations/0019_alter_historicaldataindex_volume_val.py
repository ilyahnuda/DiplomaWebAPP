# Generated by Django 4.1.5 on 2023-05-17 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0018_alter_company_chg_alter_company_percent_chg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaldataindex',
            name='volume_val',
            field=models.IntegerField(max_length=33),
        ),
    ]