# Generated by Django 4.2.11 on 2024-04-23 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoRequests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=255)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('font_color', models.CharField(max_length=255)),
                ('bg_color', models.CharField(max_length=255)),
            ],
        ),
    ]
