# Generated by Django 5.1.2 on 2024-11-08 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_foods', '0002_food_desciption_food_promotion_end_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='image_relative_url',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='desciption',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='promotion_end_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='special_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]