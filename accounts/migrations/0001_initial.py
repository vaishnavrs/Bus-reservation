# Generated by Django 5.0.1 on 2024-01-21 15:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('date', models.DateField(blank=True, default='2024-01-16')),
                ('s_time', models.TimeField(blank=True, default='00:00')),
                ('d_time', models.TimeField(blank=True, default='00:00')),
                ('price', models.IntegerField(blank=True, default=500)),
                ('n_of_seats', models.IntegerField(blank=True, default=28)),
            ],
        ),
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('selected_seat', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='accounts.bus')),
            ],
        ),
    ]
