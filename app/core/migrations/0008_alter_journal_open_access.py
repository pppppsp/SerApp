# Generated by Django 5.2 on 2025-05-19 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_journal_external_links_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='open_access',
            field=models.BooleanField(default=False, verbose_name='Тип доступа'),
        ),
    ]
