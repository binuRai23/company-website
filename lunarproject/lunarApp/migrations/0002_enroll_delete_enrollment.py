# Generated by Django 5.0.7 on 2024-08-05 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunarApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('selected_course', models.CharField(max_length=200)),
                ('course_amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Enrollment',
        ),
    ]
