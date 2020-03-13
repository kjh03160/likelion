# Generated by Django 3.0.4 on 2020-03-13 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apply_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
