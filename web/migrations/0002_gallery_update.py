# Generated by Django 4.0.3 on 2022-03-10 07:21

from django.db import migrations, models
import tinymce.models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='gallery/', verbose_name='Image')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
            ],
            options={
                'verbose_name_plural': 'Gallery',
            },
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('summary', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='updates/', verbose_name='Image')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
                ('content', tinymce.models.HTMLField(blank=True, null=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]