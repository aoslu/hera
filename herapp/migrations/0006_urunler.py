# Generated by Django 3.2.4 on 2021-07-17 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herapp', '0005_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Urunler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Urunler',
                'verbose_name_plural': 'Ürünlerim',
            },
        ),
    ]
