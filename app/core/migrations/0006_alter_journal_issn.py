# Generated by Django 5.1.4 on 2025-05-05 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_journal_links_journal_external_links'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='issn',
            field=models.CharField(max_length=255, verbose_name='Номер научного журнала'),
        ),
    ]
