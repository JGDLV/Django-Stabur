# Generated by Django 3.2.8 on 2022-02-05 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_auto_20220205_1949'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scheme',
            options={'verbose_name': 'Схема', 'verbose_name_plural': 'Схемы'},
        ),
        migrations.AlterModelOptions(
            name='schemeitem',
            options={'verbose_name': 'Пункт схемы', 'verbose_name_plural': 'Пункты схемы'},
        ),
        migrations.AlterField(
            model_name='scheme',
            name='header',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='scheme',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='scheme', to='services.service', verbose_name='Схема'),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='text_bottom',
            field=models.TextField(verbose_name='Текст внизу'),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='text_top',
            field=models.TextField(verbose_name='Текст вверху'),
        ),
    ]