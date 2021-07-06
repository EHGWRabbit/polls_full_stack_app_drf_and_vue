# Generated by Django 3.2.5 on 2021-07-06 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('no_solved_tasks', models.IntegerField()),
                ('votes', models.IntegerField(default=0)),
                ('global_ecology', models.IntegerField(default=1)),
                ('global_economic', models.IntegerField(default=1)),
                ('global_poor', models.IntegerField(default=1)),
                ('global_food', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Cry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(default='None', max_length=20, unique=True)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cry', to='main.problem')),
            ],
        ),
    ]
