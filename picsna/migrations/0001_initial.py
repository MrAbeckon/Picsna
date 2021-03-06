# Generated by Django 2.1.3 on 2018-11-10 19:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompleteV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('date_snaped', models.DateTimeField(auto_now_add=True, verbose_name='date snaped')),
            ],
        ),
        migrations.CreateModel(
            name='DetailV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=250)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='completev',
            name='contains',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='picsna.DetailV'),
        ),
    ]
