# Generated by Django 4.0.4 on 2022-06-02 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(upload_to='posts/images'),
        ),
    ]
