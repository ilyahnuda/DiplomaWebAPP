# Generated by Django 4.1.5 on 2023-04-07 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_alter_stockindex_adjclose_val_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='img_description',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
