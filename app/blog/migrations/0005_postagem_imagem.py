# Generated by Django 4.2.5 on 2023-10-03 03:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_postagem_destaque"),
    ]

    operations = [
        migrations.AddField(
            model_name="postagem",
            name="imagem",
            field=models.ImageField(blank=True, null=True, upload_to="postagens"),
        ),
    ]
