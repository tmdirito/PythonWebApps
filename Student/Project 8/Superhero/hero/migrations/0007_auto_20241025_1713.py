# Generated by Django 5.1.1 on 2024-10-25 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("hero", "0006_superhero_author"),
    ]

    operations = [
        migrations.AddField(
            model_name='superhero',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        )
    ]
