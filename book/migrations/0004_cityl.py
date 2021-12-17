# Generated by Django 4.0 on 2021-12-17 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cityl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('popluation', models.IntegerField()),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.country')),
            ],
            options={
                'verbose_name_plural': 'Cityl',
            },
        ),
    ]