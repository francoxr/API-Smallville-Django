# Generated by Django 3.2.5 on 2021-11-21 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='quote_id',
        ),
        migrations.AddField(
            model_name='quotes',
            name='author_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.author'),
            preserve_default=False,
        ),
    ]
