# Generated by Django 4.1.7 on 2023-04-01 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Loja_de_Album', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='ano_do_lancamento',
            new_name='lancamento',
        ),
    ]
