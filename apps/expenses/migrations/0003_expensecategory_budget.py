# Generated by Django 5.1.7 on 2025-03-10 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_alter_expensecategory_options_expensecategory_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='expensecategory',
            name='budget',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
    ]
