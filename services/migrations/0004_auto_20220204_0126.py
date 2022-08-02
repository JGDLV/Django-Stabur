# Generated by Django 3.2.8 on 2022-02-03 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_equipmentproperty'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipmentproperty',
            options={'verbose_name': 'Свойство', 'verbose_name_plural': 'Свойства'},
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='bucket_capacity',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='dimensions',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='drilling_depth',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='drilling_diameter',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='drive_power',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='engine_power',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='excavator_compatibility',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='feed_force',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='feeding_stroke',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='frequency',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='hole_diameter',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='hydraulic_motor_power',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='installation_weight',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='longitudinal_horizontal_pitch',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='machine_angle',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='mass_of_equipment',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='max_digging_depth',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='max_span',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='max_torque',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='maximum_breakout_force_on_bucket',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='maximum_breakout_force_on_handle',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='nominal_drilling_depth',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='operating_weight',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='operating_weight2',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='pile_dimensions',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='rotation',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='rotation_frequency',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='rotator_stroke',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='spindle_speed',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='torque',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='winch_capacity',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='working_radius',
        ),
        migrations.RemoveField(
            model_name='project',
            name='images',
        ),
        migrations.RemoveField(
            model_name='projectimage',
            name='title',
        ),
        migrations.AlterField(
            model_name='equipmentproperty',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Свойство'),
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='services.project', verbose_name='Картинка'),
        ),
    ]