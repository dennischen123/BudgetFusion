# Generated by Django 3.0.4 on 2020-03-20 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('total', models.IntegerField()),
                ('length', models.CharField(choices=[('W', 'Week'), ('M', 'Month'), ('Y', 'Year')], default='M', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Budget')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(verbose_name='expense date')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Category')),
            ],
        ),
    ]
