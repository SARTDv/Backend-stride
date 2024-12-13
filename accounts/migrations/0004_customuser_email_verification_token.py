# Generated by Django 5.1.3 on 2024-12-12 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_is_email_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='email_verification_token',
            field=models.UUIDField(blank=True, null=True, unique=True),
        ),
    ]