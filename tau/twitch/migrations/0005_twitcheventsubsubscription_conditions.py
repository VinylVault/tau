# Generated by Django 3.1.7 on 2021-07-14 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitch', '0004_twitcheventsubsubscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitcheventsubsubscription',
            name='conditions',
            field=models.JSONField(default='{}'),
            preserve_default=False,
        ),
    ]
