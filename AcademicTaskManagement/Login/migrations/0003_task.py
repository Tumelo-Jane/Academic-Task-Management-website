# Generated by Django 5.2 on 2025-04-05 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_login_details_signup_details_delete_login_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskType', models.CharField(max_length=50)),
                ('taskTittle', models.CharField(max_length=100)),
                ('subDate', models.DateField()),
                ('taskDesc', models.CharField(max_length=255)),
                ('taskReminder', models.CharField(max_length=10)),
            ],
        ),
    ]
