# Generated by Django 4.0.5 on 2022-06-09 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='web',
            field=models.URLField(blank=True, null=True),
        ),
    ]
