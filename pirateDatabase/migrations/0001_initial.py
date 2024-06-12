# Generated by Django 4.2.2 on 2023-06-19 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pirate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('born_on', models.DateField(verbose_name='Born on')),
                ('died_on', models.DateField(verbose_name='Died on')),
                ('age_at_death', models.PositiveIntegerField(verbose_name='Age at death')),
                ('cause_of_death', models.CharField(choices=[('Hanging', 'Execution By Hanging'), ('Beheading', 'Execution By Beheading'), ('Combat', 'In Combat'), ('Disease', 'Disease'), ('Unknown', 'Unknown')], default='Unknown', max_length=100, verbose_name='Cause of death')),
                ('nationality', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nationality')),
            ],
        ),
    ]
