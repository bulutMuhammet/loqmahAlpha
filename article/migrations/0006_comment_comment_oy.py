# Generated by Django 2.2.4 on 2019-08-14 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_remove_article_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_oy',
            field=models.CharField(default='Something', max_length=50),
        ),
    ]