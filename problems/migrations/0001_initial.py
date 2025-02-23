# Generated by Django 5.0.6 on 2024-07-12 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='problems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_description', models.TextField()),
                ('problem_code', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='test_cases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_code', models.CharField(max_length=10, unique=True)),
                ('test_input', models.FileField(blank=True, upload_to='testcases')),
                ('test_output', models.FileField(blank=True, upload_to='testcases')),
            ],
        ),
    ]
