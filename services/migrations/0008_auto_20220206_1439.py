# Generated by Django 3.2.8 on 2022-02-06 06:39

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_auto_20220205_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=tinymce.models.HTMLField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='text_bottom',
            field=tinymce.models.HTMLField(verbose_name='Текст внизу'),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='text_top',
            field=tinymce.models.HTMLField(verbose_name='Текст вверху'),
        ),
        migrations.AlterField(
            model_name='schemeitem',
            name='value',
            field=tinymce.models.HTMLField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=tinymce.models.HTMLField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='service',
            name='description_full',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Описание полное'),
        ),
        migrations.AlterField(
            model_name='service',
            name='equipment_text',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Текст для техники'),
        ),
        migrations.AlterField(
            model_name='service',
            name='projects_text',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Текст для проектов'),
        ),
        migrations.AlterField(
            model_name='service',
            name='types_text',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Текст для дополнительных услуг'),
        ),
        migrations.AlterField(
            model_name='type',
            name='description',
            field=tinymce.models.HTMLField(verbose_name='Описание'),
        ),
        migrations.CreateModel(
            name='ProjectProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Свойство')),
                ('value', models.CharField(blank=True, max_length=100, verbose_name='Значение')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='properties', to='services.project', verbose_name='Проект')),
            ],
            options={
                'verbose_name': 'Свойство',
                'verbose_name_plural': 'Свойства',
            },
        ),
    ]
