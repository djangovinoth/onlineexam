# Generated by Django 3.0.3 on 2020-06-07 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_answers_complted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='attemptid',
            field=models.IntegerField(),
        ),
    ]
