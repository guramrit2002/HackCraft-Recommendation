# Generated by Django 5.0.6 on 2024-06-06 10:24

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HackathonRecord',
            fields=[
                ('_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('problem_statement', models.CharField(max_length=1000)),
                ('tag', models.CharField(max_length=300)),
                ('tech', models.CharField(max_length=300)),
            ],
        ),
    ]