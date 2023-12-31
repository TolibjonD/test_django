# Generated by Django 5.0 on 2023-12-14 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('subtitle', models.CharField(max_length=550)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='media/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
