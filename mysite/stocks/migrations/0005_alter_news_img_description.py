# Generated by Django 4.1.5 on 2023-04-07 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0004_alter_news_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='img_description',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
