# Generated by Django 3.2.9 on 2022-01-18 09:10

from django.db import migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_auto_20211220_0510'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False),
        ),
    ]
