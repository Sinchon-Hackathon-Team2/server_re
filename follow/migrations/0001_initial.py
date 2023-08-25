# Generated by Django 4.2.4 on 2023-08-25 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followee_id', to=settings.AUTH_USER_MODEL)),
                ('follower_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]