# Generated by Django 2.0.1 on 2019-02-10 16:36

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_role', models.PositiveSmallIntegerField(choices=[(1, 'user'), (2, 'publisher'), (3, 'author'), (4, 'moderator'), (5, 'admin')], default=5)),
                ('phone', models.CharField(blank=True, max_length=11)),
                ('address', models.CharField(blank=True, max_length=30)),
                ('image', models.ImageField(blank=True, height_field='height_field', upload_to='', width_field='width_field')),
                ('height_field', models.IntegerField(default=255)),
                ('width_field', models.IntegerField(default=255)),
                ('fb_link', models.CharField(blank=True, max_length=100)),
                ('website', models.CharField(blank=True, max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
