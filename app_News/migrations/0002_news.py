# Generated by Django 5.0.3 on 2024-03-17 07:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_News', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=255, verbose_name='News title')),
                ('news_body', models.TextField(verbose_name='Text body')),
                ('news_image', models.ImageField(upload_to='media')),
                ('at_date', models.DateTimeField(auto_now_add=True, verbose_name='Added_time')),
                ('news_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_News.categories')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
                'db_table': 'News',
                'ordering': ['pk', 'news_title'],
                'unique_together': {('news_title', 'news_category')},
            },
        ),
    ]
