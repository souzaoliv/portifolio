# Generated by Django 4.2.6 on 2023-10-26 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0004_projetosfuncionalidades'),
    ]

    operations = [
        migrations.AddField(
            model_name='projetos',
            name='link',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]