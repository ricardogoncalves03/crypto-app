# Generated by Django 4.0 on 2021-12-29 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(blank=True, null=True)),
                ('logo', models.URLField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('market_cap', models.FloatField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
