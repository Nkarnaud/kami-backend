# Generated by Django 5.1.4 on 2025-01-03 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kamiapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airplane',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='airplane',
            unique_together={('name', 'plane_id')},
        ),
    ]
