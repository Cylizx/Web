# Generated by Django 2.0 on 2018-01-03 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dice', '0003_player_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='status',
            field=models.BooleanField(),
        ),
    ]