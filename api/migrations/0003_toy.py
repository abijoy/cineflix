# Generated by Django 4.2.1 on 2023-05-26 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_post_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('animals', 'Animals'), ('vehicles', 'Vehicles'), ('robots', 'Robots')], max_length=10)),
                ('color', models.CharField(max_length=10)),
                ('makes_sound', models.BooleanField()),
            ],
        ),
    ]