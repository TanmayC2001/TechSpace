# Generated by Django 3.0.7 on 2020-06-25 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='rating',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
