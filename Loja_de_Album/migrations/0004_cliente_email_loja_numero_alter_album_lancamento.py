# Generated by Django 4.1.7 on 2023-04-01 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Loja_de_Album', '0003_album_artista'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='loja',
            name='numero',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='lancamento',
            field=models.IntegerField(),
        ),
    ]
