# Generated by Django 2.2 on 2019-05-30 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('crm', models.CharField(max_length=50)),
                ('especialidade', models.CharField(max_length=50)),
                ('idade', models.IntegerField(max_length=2)),
            ],
        ),
    ]
