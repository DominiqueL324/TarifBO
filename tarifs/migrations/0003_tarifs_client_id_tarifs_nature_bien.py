# Generated by Django 4.1.10 on 2024-04-27 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarifs', '0002_remove_tarifs_code_remove_tarifs_commentaire_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarifs',
            name='client_id',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='tarifs',
            name='nature_bien',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
