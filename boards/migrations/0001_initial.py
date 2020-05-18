# Generated by Django 2.1 on 2018-08-22 06:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=1000)),
                ('status', models.CharField(choices=[('draft', '待定'), ('active', '激活'), ('inactive', '无效'), ('deleted', '已删除')], default='active', max_length=8)),
                ('start', models.DateTimeField(default=django.utils.timezone.now)),
                ('end', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.CharField(max_length=1000)),
                ('status', models.CharField(choices=[('draft', '待定'), ('active', '激活'), ('inactive', '无效'), ('deleted', '已删除')], default='active', max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=4000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('post_type', models.CharField(default='post', max_length=1000)),
                ('status', models.CharField(choices=[('draft', '待定'), ('active', '激活'), ('inactive', '无效'), ('deleted', '已删除')], default='active', max_length=8)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField(max_length=1000)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(choices=[('draft', '待定'), ('active', '激活'), ('inactive', '无效'), ('deleted', '已删除')], default='active', max_length=8)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='topics', to='boards.Board')),
                ('starter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='topics', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='boards.Topic'),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='board',
            name='entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='boards', to='boards.Entity'),
        ),
    ]
