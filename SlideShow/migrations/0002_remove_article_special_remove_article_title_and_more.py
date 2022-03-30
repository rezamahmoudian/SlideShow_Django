# Generated by Django 4.0.3 on 2022-03-30 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SlideShow', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='special',
        ),
        migrations.RemoveField(
            model_name='article',
            name='title',
        ),
        migrations.AddField(
            model_name='article',
            name='title_en',
            field=models.CharField(default=0, max_length=200, verbose_name='عنوان'),
        ),
        migrations.AddField(
            model_name='article',
            name='title_fa',
            field=models.CharField(default=0, max_length=200, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('p', 'منتشر شده'), ('d', 'پیش نویس')], max_length=1, verbose_name='وضعیت'),
        ),
    ]