# Generated by Django 5.1.2 on 2024-10-31 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viridian_accesibility', '0002_withdrawal_assets_alter_deposit_assets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='withdrawal',
            name='amount',
        ),
        migrations.AddField(
            model_name='withdrawal',
            name='tx_hash',
            field=models.CharField(default='', max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deposit',
            name='tx_hash',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='referral',
            unique_together={('referral', 'datetime', 'user_address')},
        ),
    ]