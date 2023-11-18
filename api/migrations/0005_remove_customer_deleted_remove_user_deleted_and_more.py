# Generated by Django 4.2.7 on 2023-11-18 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_customer_deleted_at_alter_user_deleted_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='user',
            name='deleted',
        ),
        migrations.AlterField(
            model_name='customer',
            name='deleted_at',
            field=models.DateTimeField(blank=True, default=None, editable=False, null=True, verbose_name='deleted date'),
        ),
        migrations.AlterField(
            model_name='user',
            name='deleted_at',
            field=models.DateTimeField(blank=True, default=None, editable=False, null=True, verbose_name='deleted date'),
        ),
    ]