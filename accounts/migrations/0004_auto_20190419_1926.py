# Generated by Django 2.1.7 on 2019-04-19 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190419_0425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestemail',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
