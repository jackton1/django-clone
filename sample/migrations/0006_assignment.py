# Generated by Django 3.0.1 on 2020-05-12 19:57

from django.db import migrations, models
import model_clone.mixins.clone


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0005_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Job title')),
                ('assignment_date', models.DateField(blank=True, null=True)),
                ('assignment_status', models.CharField(blank=True, choices=[(1, 'Complete'), (2, 'Incomplete')], default='O', max_length=2, verbose_name='Assignment status')),
                ('location', models.CharField(max_length=25, null=True, verbose_name='Location')),
                ('driver_type', models.CharField(choices=[(1, 'Commercial'), (2, 'Residential')], max_length=2, null=True, verbose_name='Driver type')),
                ('car_type', models.CharField(choices=[(1, 'Large'), (2, 'Small')], max_length=2, null=True, verbose_name='Car type')),
                ('compensation', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Compensation')),
                ('hours', models.IntegerField(null=True, verbose_name='Amount of hours')),
                ('spots_available', models.IntegerField(null=True, verbose_name='Spots available')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Assignment description')),
            ],
            options={
                'verbose_name': 'Assigment',
                'verbose_name_plural': 'Assignments',
            },
            bases=(model_clone.mixins.clone.CloneMixin, models.Model),
        ),
    ]