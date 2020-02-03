# Generated by Django 3.0.2 on 2020-02-02 00:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('programLibrary', '0004_auto_20200201_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='html',
            name='id',
            field=models.UUIDField(default=uuid.UUID('aaba26d5-a29e-443e-8c85-13d8faaa9664'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='mcq',
            name='id',
            field=models.UUIDField(default=uuid.UUID('7e6118b1-da87-4570-a3c5-227896f02151'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ba94c335-d838-4421-8c18-26e4f45b5a21'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='id',
            field=models.UUIDField(default=uuid.UUID('f9587f9d-fac8-46c5-b259-dc0754160b0c'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]