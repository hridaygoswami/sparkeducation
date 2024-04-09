# Generated by Django 5.0.2 on 2024-03-13 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sparkwebadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=20)),
                ('content', models.CharField(max_length=20)),
                ('img1', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('link1', models.CharField(max_length=30)),
                ('link2', models.CharField(max_length=30)),
            ],
        ),
    ]