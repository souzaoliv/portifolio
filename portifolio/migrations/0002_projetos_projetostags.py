# Generated by Django 4.2.6 on 2023-10-23 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projetos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.TextField(max_length=1000)),
                ('imagem', models.ImageField(upload_to='portifolio/static/portifolio/img')),
            ],
        ),
        migrations.CreateModel(
            name='ProjetosTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portifolio.projetos')),
            ],
        ),
    ]
