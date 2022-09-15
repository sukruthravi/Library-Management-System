# Generated by Django 4.1 on 2022-09-14 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100, unique=True)),
                ('author_name', models.CharField(max_length=100)),
                ('book_summary', models.CharField(max_length=300)),
            ],
        ),
    ]
