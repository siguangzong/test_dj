# Generated by Django 3.1.6 on 2021-02-08 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='姓名')),
                ('sex', models.CharField(max_length=20, verbose_name='性别')),
            ],
        ),
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=63, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='书名')),
                ('price', models.IntegerField(verbose_name='价格')),
                ('color', models.CharField(max_length=64, verbose_name='颜色')),
                ('page_num', models.IntegerField(null=True, verbose_name='页数')),
                ('author', models.ManyToManyField(to='learn.Author', verbose_name='作者')),
                ('publisher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='learn.publish', verbose_name='发布者')),
            ],
        ),
    ]
