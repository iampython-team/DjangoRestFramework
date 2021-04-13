# Generated by Django 3.1.4 on 2021-03-17 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=50)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
    ]