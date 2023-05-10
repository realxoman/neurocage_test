# Generated by Django 4.2.1 on 2023-05-10 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=256, verbose_name='Label')),
                ('color', models.CharField(blank=True, max_length=50, null=True, verbose_name='Cage Colour')),
                ('material', models.CharField(blank=True, max_length=50, null=True, verbose_name='Cage Material')),
                ('version', models.CharField(blank=True, max_length=10, null=True, verbose_name='Cage Version')),
                ('dimensions', models.CharField(blank=True, max_length=50, null=True, verbose_name='Cage Dimensions')),
            ],
            options={
                'verbose_name': 'Cage',
                'verbose_name_plural': 'Cages',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='CageAnalytical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'N/A'), (1, 'Bad'), (2, 'Ok'), (3, 'Perfect')], verbose_name='Cage Status')),
                ('time_taken', models.PositiveIntegerField(default=0, verbose_name='Time Taken')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Cage Creation Time')),
                ('cage_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cage_related', to='cages.cage', verbose_name='Cage Id')),
            ],
            options={
                'verbose_name': 'Cage Analytical',
                'verbose_name_plural': 'Cage Analytics',
                'ordering': ('-created_at',),
            },
        ),
    ]