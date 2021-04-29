# Generated by Django 3.1.4 on 2021-04-24 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email поле')),
                ('first_name', models.CharField(max_length=150, verbose_name='Імя користувача')),
                ('last_name', models.CharField(max_length=150, verbose_name='Прізвище користувача')),
                ('username', models.CharField(max_length=150, verbose_name='Нік користувача')),
                ('is_editor', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='UserExtend',
        ),
    ]
