# Generated by Django 4.2.1 on 2023-05-10 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name="user", name="first_name", field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(
                default=True,
                help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                verbose_name="active",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(
                default=False,
                help_text="Designates whether the user can log into this admin site.",
                verbose_name="staff status",
            ),
        ),
        migrations.AlterField(
            model_name="user", name="last_name", field=models.CharField(max_length=50),
        ),
    ]