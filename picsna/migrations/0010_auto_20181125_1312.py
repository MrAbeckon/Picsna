# Generated by Django 2.1.3 on 2018-11-25 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picsna', '0009_auto_20181125_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailv',
            name='picture',
            field=models.ImageField(null=True, upload_to='picsna/static/images/detail_view'),
        ),
    ]
