# Generated by Django 4.1.7 on 2023-06-14 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_usuario_autenticacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='foto',
        ),
        migrations.AddField(
            model_name='usuario',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='img_usuario', verbose_name=''),
        ),
    ]