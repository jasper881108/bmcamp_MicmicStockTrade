# Generated by Django 3.1.5 on 2021-05-04 07:29

from django.db import migrations, models
import member.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='Email')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='User')),
                ('money', models.DecimalField(decimal_places=2, default=1000.0, max_digits=30, verbose_name='Money')),
                ('date_joined', models.DateField(auto_now_add=True, verbose_name='Join Date')),
                ('last_login', models.DateField(auto_now=True, verbose_name='Last Used')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Admin')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='SuperUser')),
                ('profile_image', models.ImageField(blank=True, default=member.models.get_default_profile_image, max_length=255, null=True, upload_to=member.models.get_profile_image_path)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
