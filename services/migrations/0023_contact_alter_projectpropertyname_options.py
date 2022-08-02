# Generated by Django 4.0.4 on 2022-06-05 05:06

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0022_projectproperty_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ceo', models.CharField(max_length=100, verbose_name='Директор')),
                ('full_name', models.CharField(max_length=250, verbose_name='Полное наименование организации')),
                ('left', tinymce.models.HTMLField(verbose_name='Левая колонка')),
                ('right', tinymce.models.HTMLField(verbose_name='Правая колонка')),
            ],
            options={
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.AlterModelOptions(
            name='projectpropertyname',
            options={'verbose_name': 'Свойство проекта', 'verbose_name_plural': 'Свойства проекта'},
        ),
    ]
