# Generated by Django 4.1 on 2022-08-30 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="descipcion",
            field=models.TextField(),
        ),
    ]