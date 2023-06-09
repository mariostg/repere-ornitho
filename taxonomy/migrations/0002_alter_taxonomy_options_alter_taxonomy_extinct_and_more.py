# Generated by Django 4.2.2 on 2023-06-13 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taxonomy", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="taxonomy",
            options={"verbose_name_plural": "Taxonomie"},
        ),
        migrations.AlterField(
            model_name="taxonomy",
            name="extinct",
            field=models.CharField(max_length=75, verbose_name="éteint"),
        ),
        migrations.AlterField(
            model_name="taxonomy",
            name="extinctYear",
            field=models.CharField(max_length=75, verbose_name="année d'extinction"),
        ),
        migrations.AlterField(
            model_name="taxonomy",
            name="reportAs",
            field=models.CharField(max_length=75, verbose_name="rapport"),
        ),
    ]
