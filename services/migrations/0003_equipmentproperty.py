# Generated by Django 3.2.8 on 2022-02-03 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20220203_2340'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('value', models.CharField(blank=True, max_length=100, verbose_name='Значение')),
                ('position', models.SmallIntegerField(default=999, verbose_name='Позиция')),
                ('equipment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='properties', to='services.equipment', verbose_name='Техника')),
            ],
        ),
    ]
