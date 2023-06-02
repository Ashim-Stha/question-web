# Generated by Django 4.1.4 on 2023-05-29 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ioecropedquestionpaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('croppedno', models.IntegerField()),
                ('faculty', models.CharField(max_length=4)),
                ('semester', models.IntegerField()),
                ('year', models.IntegerField()),
                ('imagecropped', models.BinaryField()),
                ('desc', models.TextField()),
                ('keyword', models.TextField()),
            ],
        ),
    ]