# Generated by Django 4.0.6 on 2022-08-10 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_alter_event_address_alter_event_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='address',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(help_text='Enter Category', max_length=20),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_time',
            field=models.DateTimeField(help_text='Enter date of event'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(help_text='Enter Description', max_length=350),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='event',
            name='pImage',
            field=models.ImageField(help_text='Enter Pimage', upload_to=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='phone',
            field=models.CharField(help_text='Enter Telephone no.', max_length=50),
        ),
    ]
