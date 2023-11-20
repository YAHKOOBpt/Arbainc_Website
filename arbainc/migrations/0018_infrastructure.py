# Generated by Django 4.2.6 on 2023-10-30 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arbainc', '0017_construction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Infrastructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='Infrastructure/')),
            ],
        ),
    ]
