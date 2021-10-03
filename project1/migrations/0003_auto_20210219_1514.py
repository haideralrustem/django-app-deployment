# Generated by Django 3.0.8 on 2021-02-19 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0002_auto_20210218_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tabulardatasets',
            name='dataset_row',
        ),
        migrations.AddField(
            model_name='mycsvrow',
            name='parent_dataset_table',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='project1.TabularDataSets'),
            preserve_default=False,
        ),
    ]
