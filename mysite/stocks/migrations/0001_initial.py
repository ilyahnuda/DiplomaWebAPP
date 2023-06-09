# Generated by Django 4.1.5 on 2023-04-07 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('symbol', models.CharField(max_length=10)),
                ('weight', models.DecimalField(decimal_places=10, max_digits=19)),
                ('price', models.DecimalField(decimal_places=10, max_digits=19)),
                ('chg', models.DecimalField(decimal_places=10, max_digits=19)),
                ('percent_chg', models.DecimalField(decimal_places=10, max_digits=19)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('time_news', models.DateTimeField()),
                ('img', models.ImageField(null=True, upload_to='')),
                ('text', models.TextField()),
                ('img_description', models.CharField(max_length=100, null=True)),
                ('link', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StockIndex',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField()),
                ('open_val', models.DecimalField(decimal_places=6, max_digits=12)),
                ('high_val', models.DecimalField(decimal_places=6, max_digits=12)),
                ('low_val', models.DecimalField(decimal_places=6, max_digits=12)),
                ('close_val', models.DecimalField(decimal_places=6, max_digits=12)),
                ('adjclose_val', models.DecimalField(decimal_places=6, max_digits=12)),
                ('volume_val', models.DecimalField(decimal_places=6, max_digits=12)),
                ('symbol', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stocks.company')),
            ],
        ),
    ]
