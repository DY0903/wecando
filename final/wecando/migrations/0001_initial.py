# Generated by Django 4.2.6 on 2023-11-01 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('test_num', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]