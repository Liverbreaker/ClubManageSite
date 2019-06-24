# Generated by Django 2.2.2 on 2019-06-23 07:48

from django.db import migrations, models
import django.db.models.deletion
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users_mgt', '0001_initial'),
        ('club_mgt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('begin', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('deadline', models.DateTimeField()),
                ('content', djrichtextfield.models.RichTextField()),
                ('site', models.CharField(max_length=40)),
                ('contact', models.TextField()),
                ('fee', models.IntegerField()),
                ('meal', models.BooleanField(default=False)),
                ('insure', models.BooleanField(default=True)),
                ('note', djrichtextfield.models.RichTextField()),
                ('log_add_time', models.DateTimeField(auto_now_add=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('is_activate', models.BooleanField(default=True)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club_mgt.Club')),
                ('principal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club_mgt.Member')),
            ],
            options={
                'ordering': ['-timestamp'],
                'permissions': (('can_view', 'Can view Activity'), ('can_add', 'Can add Activity'), ('can_edit', 'Can edit Activity'), ('can_close', 'Can close Activity'), ('can_delete', 'Can delete Activity')),
            },
        ),
        migrations.CreateModel(
            name='Activity_join',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('log_add_time', models.DateTimeField(auto_now_add=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('act_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity_mgt.Activity')),
                ('attender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users_mgt.Student')),
            ],
            options={
                'ordering': ['-timestamp'],
                'permissions': (('can_view', 'Can view Activity_join'), ('can_add', 'Can add Activity_join'), ('can_edit', 'Can edit Activity_join'), ('can_delete', 'Can delete Activity_join')),
            },
        ),
    ]