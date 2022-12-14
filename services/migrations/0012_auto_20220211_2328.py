# Generated by Django 3.2.8 on 2022-02-11 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_auto_20220209_2302'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scheme',
            options={'verbose_name': 'Схема работы', 'verbose_name_plural': 'Схемы работы'},
        ),
        migrations.RenameField(
            model_name='type',
            old_name='scheme',
            new_name='service',
        ),
        migrations.AlterField(
            model_name='equipment',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Цена'),
        ),
    ]
