# Generated by Django 2.0.4 on 2018-04-13 00:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('badpress', '0002_auto_20180410_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('link', models.CharField(max_length=250)),
                ('sentiment_score', models.CharField(max_length=250)),
                ('summary', models.TextField(help_text='Enter a brief description of the book', max_length=1000)),
                ('date', models.DateField(blank=True, null=True)),
                ('title', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('place_birth', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('URL_photo', models.CharField(max_length=250)),
                ('party', models.CharField(max_length=100)),
                ('score_issue_1', models.IntegerField()),
                ('score_issue_2', models.IntegerField()),
                ('score_issue_3', models.IntegerField()),
                ('score_issue_4', models.IntegerField()),
                ('score_issue_5', models.IntegerField()),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('info', models.TextField(max_length=1000)),
                ('URL_logo', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('URL_logo', models.CharField(max_length=250)),
            ],
        ),
        migrations.RemoveField(
            model_name='state',
            name='state_name',
        ),
        migrations.AddField(
            model_name='state',
            name='URL_logo',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='state',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='state',
            name='primaries_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='candidate',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='badpress.State'),
        ),
        migrations.AddField(
            model_name='article',
            name='candidate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='badpress.Candidate'),
        ),
        migrations.AddField(
            model_name='article',
            name='issue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='badpress.Issue'),
        ),
        migrations.AddField(
            model_name='article',
            name='source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='badpress.Source'),
        ),
        migrations.AddField(
            model_name='article',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='badpress.State'),
        ),
    ]
