# Generated by Django 5.1.2 on 2024-10-31 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viridian_accesibility', '0003_remove_withdrawal_amount_withdrawal_tx_hash_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('referral', models.IntegerField()),
                ('user', models.CharField(max_length=100)),
            ],
            options={
                'unique_together': {('start', 'end', 'referral', 'user')},
            },
        ),
    ]