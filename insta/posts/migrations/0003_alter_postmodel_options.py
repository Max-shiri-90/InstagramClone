# Generated by Django 4.0.4 on 2022-06-02 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_postmodel_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postmodel',
            options={'verbose_name': 'Post'},
        ),
    ]
