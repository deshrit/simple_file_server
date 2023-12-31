# Generated by Django 4.2.2 on 2023-06-24 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.DateTimeField(auto_now=True)),
                ('file_name', models.CharField(max_length=254)),
                ('file_ext', models.CharField(max_length=50)),
                ('blob_name', models.CharField(db_index=True, max_length=37)),
                ('file_url', models.CharField(max_length=254)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
