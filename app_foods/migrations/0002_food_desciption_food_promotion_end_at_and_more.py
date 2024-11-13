# Generated by Django 5.1.2 on 2024-10-30 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_foods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='desciption',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='promotion_end_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='special_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='is_premium',
            field=models.BooleanField(default=True),
        ),
    ]
