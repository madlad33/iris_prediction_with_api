# Generated by Django 3.2.4 on 2021-06-24 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sepal_length', models.FloatField()),
                ('sepal_width', models.FloatField()),
                ('petal_length', models.FloatField()),
                ('petal_width', models.FloatField()),
                ('classification', models.CharField(max_length=33)),
            ],
        ),
    ]
