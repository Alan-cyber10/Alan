# Generated by Django 5.1.4 on 2025-01-07 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(upload_to='user_profile'),
        ),
    ]
