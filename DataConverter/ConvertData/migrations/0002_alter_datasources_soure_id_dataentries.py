# Generated by Django 5.1.4 on 2025-01-01 18:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ConvertData', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasources',
            name='soure_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='DataEntries',
            fields=[
                ('entry_id', models.IntegerField(primary_key=True, serialize=False)),
                ('source_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConvertData.datasources')),
            ],
        ),
    ]