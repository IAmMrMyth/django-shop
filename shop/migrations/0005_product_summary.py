# Generated by Django 4.1 on 2022-12-29 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0004_remove_product_color_product_color"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="summary",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
    ]