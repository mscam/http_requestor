# Generated by Django 3.0.11 on 2020-12-22 01:36

from django.db import migrations, models
import django.db.models.deletion
import http_requestor.core.fields
import http_requestor.core.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HttpRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('method', models.CharField(choices=[('get', 'Get'), ('head', 'Head'), ('post', 'Post'), ('put', 'Put'), ('delete', 'Delete')], max_length=8)),
                ('headers', http_requestor.core.fields.JSONField(blank=True, default='{}')),
                ('params', http_requestor.core.fields.JSONField(blank=True, default='{}')),
                ('data', http_requestor.core.fields.JSONField(blank=True, default='{}')),
                ('schedule_at', models.DateTimeField(validators=[http_requestor.core.models.validate_schedule_at])),
                ('task_id', models.CharField(blank=True, editable=False, max_length=36)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='HttpResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_code', models.PositiveIntegerField()),
                ('headers', http_requestor.core.fields.JSONField(default='{}')),
                ('text', models.TextField(blank=True)),
                ('request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.HttpRequest')),
            ],
        ),
    ]