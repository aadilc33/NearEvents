# Generated by Django 4.0.6 on 2022-08-10 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_imagestore_alter_event_pimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='pImage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.imagestore'),
        ),
    ]
