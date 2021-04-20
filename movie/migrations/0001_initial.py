# Generated by Django 3.1.7 on 2021-04-17 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('number', models.CharField(blank=True, max_length=10, null=True)),
                ('dob', models.DateField(blank=True, max_length=200, null=True)),
                ('website', models.URLField(blank=True, max_length=230, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female'), ('others', 'others')], max_length=30, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('prefix', models.CharField(blank=True, max_length=500, null=True)),
                ('website', models.URLField(blank=True, max_length=500, null=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('prefix', models.CharField(blank=True, max_length=500, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=500, null=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('review', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('director', models.ManyToManyField(blank=True, to='movie.Director')),
                ('genre', models.ManyToManyField(blank=True, to='movie.Genre')),
                ('studio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.studio')),
            ],
        ),
    ]
