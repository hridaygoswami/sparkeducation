# Generated by Django 4.2.5 on 2024-04-22 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sparkwebadmin', '0009_remove_about_img2_remove_about_link1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=20)),
                ('content', models.CharField(max_length=20)),
                ('img1', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('img3', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('img4', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('img5', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('img6', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
