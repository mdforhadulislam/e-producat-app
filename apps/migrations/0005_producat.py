# Generated by Django 4.0.3 on 2023-10-10 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_propuler_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='hello', max_length=20)),
                ('title', models.CharField(default='hello', max_length=40)),
                ('status_categories', models.CharField(default='hello', max_length=40)),
                ('availability', models.BooleanField(default=True)),
                ('producat_tags', models.CharField(default='hello', max_length=30, null=True)),
                ('producat_image_1', models.ImageField(blank=True, null=True, upload_to='producats/')),
                ('producat_image_2', models.ImageField(blank=True, null=True, upload_to='producats/')),
                ('producat_image_3', models.ImageField(blank=True, null=True, upload_to='producats/')),
                ('producat_image_4', models.ImageField(blank=True, null=True, upload_to='producats/')),
                ('producat_description', models.TextField(blank=True, default='helloooooo', null=True)),
                ('discount_percent', models.CharField(default='30%', max_length=4, null=True)),
                ('prices', models.CharField(default='0000', max_length=10)),
            ],
        ),
    ]