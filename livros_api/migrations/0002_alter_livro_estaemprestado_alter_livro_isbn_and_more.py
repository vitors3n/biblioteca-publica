# Generated by Django 5.1.2 on 2024-10-26 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='estaEmprestado',
            field=models.BooleanField(default=False, verbose_name='Está emprestado?'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='isbn',
            field=models.CharField(max_length=13, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='titulo',
            field=models.CharField(max_length=255, verbose_name='Título'),
        ),
    ]