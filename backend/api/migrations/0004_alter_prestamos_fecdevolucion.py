# Generated by Django 3.2.9 on 2021-11-15 00:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20211114_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamos',
            name='fecDevolucion',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
