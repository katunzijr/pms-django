# Generated by Django 4.1.7 on 2023-03-23 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('settings', '0001_initial'),
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='in_pharmacy',
            field=models.ForeignKey(db_column='in_pharmacy', on_delete=django.db.models.deletion.CASCADE, to='settings.pharmacy'),
        ),
    ]
