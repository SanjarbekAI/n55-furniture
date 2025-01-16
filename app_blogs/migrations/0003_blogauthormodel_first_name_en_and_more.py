# Generated by Django 5.1.4 on 2025-01-16 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blogs', '0002_blogcommentmodel_blog_alter_blogcommentmodel_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogauthormodel',
            name='first_name_en',
            field=models.CharField(max_length=128, null=True, verbose_name='first_name'),
        ),
        migrations.AddField(
            model_name='blogauthormodel',
            name='first_name_uz',
            field=models.CharField(max_length=128, null=True, verbose_name='first_name'),
        ),
        migrations.AddField(
            model_name='blogauthormodel',
            name='last_name_en',
            field=models.CharField(max_length=128, null=True, verbose_name='last_name'),
        ),
        migrations.AddField(
            model_name='blogauthormodel',
            name='last_name_uz',
            field=models.CharField(max_length=128, null=True, verbose_name='last_name'),
        ),
        migrations.AddField(
            model_name='blogcategorymodel',
            name='title_en',
            field=models.CharField(max_length=128, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='blogcategorymodel',
            name='title_uz',
            field=models.CharField(max_length=128, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='description_en',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='description_uz',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='title_en',
            field=models.CharField(max_length=128, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='title_uz',
            field=models.CharField(max_length=128, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='blogtagmodel',
            name='title_en',
            field=models.CharField(max_length=128, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='blogtagmodel',
            name='title_uz',
            field=models.CharField(max_length=128, null=True, verbose_name='title'),
        ),
    ]
