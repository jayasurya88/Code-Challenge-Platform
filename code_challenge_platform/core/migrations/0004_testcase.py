# Generated by Django 5.1.2 on 2024-10-27 04:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_challenge'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_data', models.TextField()),
                ('expected_output', models.TextField()),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_cases', to='core.challenge')),
            ],
        ),
    ]
