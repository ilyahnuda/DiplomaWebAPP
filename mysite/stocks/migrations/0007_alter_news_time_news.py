# Generated by Django 4.1.5 on 2023-04-07 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0006_alter_news_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='time_news',
            field=models.CharField(max_length=100),
        ),
    ]
