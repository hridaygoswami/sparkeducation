# Generated by Django 5.0.2 on 2024-03-13 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sparkwebadmin', '0003_course1'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('number', models.CharField(blank=True, max_length=15, null=True)),
                ('category', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=20)),
            ],
        ),
    ]
