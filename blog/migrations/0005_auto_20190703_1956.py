# Generated by Django 2.2.2 on 2019-07-03 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('blog', '0004_post_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='creator',
            field=models.ManyToManyField(blank=True, related_name='tags', to='user.Profile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='creator',
            field=models.ManyToManyField(blank=True, related_name='posts', to='user.Profile'),
        ),
    ]
