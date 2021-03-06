# Generated by Django 2.2.3 on 2019-07-12 05:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True, verbose_name='Дата/Время')),
                ('text', models.TextField(verbose_name='Сообщение')),
                ('last', models.BooleanField(default=True)),
                ('recipient', models.ManyToManyField(blank=True, related_name='messages', to='messager.Sender', verbose_name='Получатель')),
                ('sender', models.OneToOneField(default=1000, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Отправитель')),
            ],
        ),
    ]
