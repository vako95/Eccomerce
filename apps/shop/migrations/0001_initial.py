# Generated by Django 5.2 on 2025-04-23 20:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter the product title (max 255 characters).', max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(blank=True, help_text='Automatically generated based on the Title.', max_length=255, unique=True, verbose_name='Slug')),
                ('content', models.TextField(blank=True, help_text='Content about product', verbose_name='Content')),
                ('poster', models.FileField(blank=True, help_text='Upload an image', null=True, upload_to='%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png', 'webp'])], verbose_name='Poster')),
                ('price', models.FloatField(default=0.0, help_text='Enter a value between 0 and 10,000,000.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Price')),
                ('discount', models.IntegerField(blank=True, default=0, help_text='Enter a value from 0 to 100.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Discount (%)')),
                ('tax', models.FloatField(blank=True, default=0.0, help_text='Enter tax amount (0–10,000,000).', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000000)], verbose_name='Tax')),
                ('status', models.BooleanField(default=True, help_text='Indicates whether the item is active.', verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date and time when the item was created.', verbose_name='Created At')),
                ('update_at', models.DateTimeField(auto_now=True, help_text='Date and time of the last update.', verbose_name='Last Updated')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ('-created_at',),
            },
        ),
    ]
