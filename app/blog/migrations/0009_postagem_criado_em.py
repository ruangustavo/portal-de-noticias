# Generated by Django 4.2.5 on 2023-11-26 21:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0008_postagem_atualizado_em"),
    ]

    operations = [
        migrations.AddField(
            model_name="postagem",
            name="criado_em",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
