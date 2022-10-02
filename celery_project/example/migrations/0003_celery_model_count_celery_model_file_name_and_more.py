# Generated by Django 4.1.1 on 2022-10-02 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0002_alter_celery_model_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='celery_model',
            name='count',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='celery_model',
            name='file_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='celery_model',
            name='status',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='celery_model',
            name='task_id',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
