# Generated by Django 4.2.2 on 2024-06-05 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_subject_subjectmarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectmarks',
            name='marks',
            field=models.IntegerField(),
        ),
    ]
