# Generated by Django 4.2.7 on 2023-11-18 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_customer_deleted_at_alter_user_deleted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
    ]
