# Generated by Django 2.1.3 on 2018-11-10 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picsna', '0005_auto_20181110_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completev',
            name='picture',
            field=models.ImageField(null=True, upload_to='picsna/static/images/complete_view'),
        ),
        migrations.AlterField(
            model_name='detailv',
            name='picture',
            field=models.ImageField(null=True, upload_to='picsna/static/images/detail_view'),
        ),
    ]
