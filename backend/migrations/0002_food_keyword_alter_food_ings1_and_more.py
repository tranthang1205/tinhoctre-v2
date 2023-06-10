# Generated by Django 4.2.1 on 2023-06-09 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='keyword',
            field=models.CharField(default='Some String', max_length=50, verbose_name='Keyword'),
        ),
        migrations.AlterField(
            model_name='food',
            name='ings1',
            field=models.ManyToManyField(through='backend.Food_Ingredient', to='backend.ingredient', verbose_name='nguyen lieu'),
        ),
        migrations.AlterField(
            model_name='food_ingredient',
            name='food_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredient', to='backend.food', verbose_name='food'),
        ),
    ]