# Generated by Django 3.1.7 on 2021-04-01 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_foto', models.CharField(max_length=255)),
                ('slug', models.ImageField(upload_to='galeria')),
                ('foto', models.ImageField(upload_to='galeria')),
            ],
        ),
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200)),
                ('preco', models.FloatField()),
                ('imagem', models.ImageField(upload_to='chaFraldas')),
            ],
        ),
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('mensagem', models.TextField()),
            ],
        ),
    ]