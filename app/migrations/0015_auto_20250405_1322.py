# Generated by Django 3.2.25 on 2025-04-05 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_familymember_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familymember',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='familymember',
            name='rationcard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.rationcard'),
        ),
    ]
