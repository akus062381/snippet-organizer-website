# Generated by Django 3.0.6 on 2020-06-02 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippet', '0003_auto_20200602_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
