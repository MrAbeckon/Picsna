# Generated by Django 2.1.3 on 2018-11-27 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picsna', '0011_auto_20181127_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completev',
            name='picture',
            field=models.ImageField(default='default.png', upload_to='picsna/static/images/complete_view'),
        ),
        migrations.AlterField(
            model_name='detailv',
            name='picture',
            field=models.ImageField(default='default.png', upload_to='picsna/static/images/detail_view'),
        ),
    ]
