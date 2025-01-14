# Generated by Django 3.2.9 on 2021-11-24 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(max_length=255)),
                ('correta', models.BooleanField(default=False)),
                ('questao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questao.questao')),
            ],
        ),
    ]
