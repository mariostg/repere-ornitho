# Generated by Django 4.2.2 on 2023-06-25 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("geographie", "0002_municipalite_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="municipalite",
            name="code",
            field=models.CharField(max_length=8, verbose_name="Code de MRC"),
        ),
    ]
