# Generated by Django 4.1.6 on 2023-02-10 13:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0002_rename_seller_meroshare_linked_to'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('appliedby_name', models.CharField(max_length=100)),
                ('applied_company', models.CharField(max_length=100)),
                ('applied_on', models.DateTimeField(auto_now_add=True)),
                ('linked_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
