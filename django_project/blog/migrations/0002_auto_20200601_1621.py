# Generated by Django 2.2.7 on 2020-06-01 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='question1',
            new_name='question',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='question10',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='question2',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='question3',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='question4',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='question5',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='question6',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='question7',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='question8',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='question9',
        ),
    ]
