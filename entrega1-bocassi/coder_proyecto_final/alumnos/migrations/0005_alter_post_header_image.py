# Generated by Django 4.1.1 on 2022-10-02 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0004_post_header_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/'),
        ),
    ]