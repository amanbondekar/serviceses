# Generated by Django 4.1.7 on 2023-02-23 11:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.RegexValidator('^[a-zA-Z ]+$', 'Name can only contain letters and spaces.')])),
                ('location', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('IT', 'IT'), ('non IT', 'non IT'), ('mobile phones', 'mobile phones')], max_length=100)),
                ('added_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='employee_images')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.RegexValidator('^[a-zA-Z ]+$', 'Name can only contain letters and spaces.')])),
                ('email', models.EmailField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('about', models.TextField()),
                ('position', models.CharField(choices=[('manager', 'manager'), ('softwere Developer', 'sd'), ('Project Leader', 'pl')], max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company')),
                ('images', models.ManyToManyField(to='api.image')),
            ],
        ),
    ]