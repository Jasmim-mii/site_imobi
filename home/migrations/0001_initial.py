# Generated by Django 4.0.2 on 2022-02-02 21:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='Real_estate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('room', models.IntegerField()),
                ('dimension', models.FloatField()),
                ('street', models.CharField(max_length=50)),
                ('location', models.CharField(choices=[('V', 'Venda'), ('A', 'Alguel')], max_length=1)),
                ('type_imovel', models.CharField(choices=[('A', 'Apartamento'), ('C', 'Casa')], max_length=1)),
                ('number', models.IntegerField()),
                ('describe', models.TextField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.city')),
                ('image', models.ManyToManyField(to='home.Image')),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Visualization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_Visualization', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_select', models.CharField(max_length=20)),
                ('time_visualization', models.TimeField()),
                ('status', models.CharField(choices=[('A', 'Agendado'), ('F', 'Finalizado'), ('C', 'Cancelado')], default='A', max_length=1)),
                ('imovel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.real_estate')),
                ('user_visualization', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='real_estate',
            name='time',
            field=models.ManyToManyField(to='home.Time'),
        ),
        migrations.AddField(
            model_name='real_estate',
            name='visualization_day',
            field=models.ManyToManyField(to='home.Visualization'),
        ),
    ]
