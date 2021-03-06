# Generated by Django 2.1.3 on 2018-12-16 17:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('picsna', '0017_detailv_completev'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date snaped')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='detailv',
            name='completev',
        ),
        migrations.DeleteModel(
            name='CompleteV',
        ),
        migrations.AddField(
            model_name='comment',
            name='detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='picsna.DetailV'),
        ),
    ]
