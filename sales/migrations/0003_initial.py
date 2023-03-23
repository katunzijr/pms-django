# Generated by Django 4.1.7 on 2023-03-23 10:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sales', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='owner',
            field=models.ForeignKey(db_column='owner', on_delete=django.db.models.deletion.DO_NOTHING, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='records',
            name='trans_by',
            field=models.ForeignKey(db_column='tran_by', on_delete=django.db.models.deletion.DO_NOTHING, related_name='tran_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
