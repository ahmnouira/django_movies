# Generated by Django 4.0.5 on 2022-06-02 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='movies/images')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]