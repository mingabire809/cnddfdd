# Generated by Django 3.2.6 on 2021-12-02 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('antenne', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('firstName', models.CharField(max_length=60, verbose_name='First Name')),
                ('lastName', models.CharField(max_length=60, verbose_name='Last Name')),
                ('phoneNumber', models.IntegerField(null=True, unique=True, verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=60, primary_key=True, serialize=False, unique=True, verbose_name='email')),
                ('antenne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='antenne.antenne', verbose_name='Antenne belonging to')),
            ],
        ),
    ]
