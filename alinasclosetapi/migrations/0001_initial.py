# Generated by Django 3.2.4 on 2021-06-16 20:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Look',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('look_name', models.CharField(max_length=50)),
                ('note', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('piece_name', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=50)),
                ('imageurl', models.ImageField(upload_to=None)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alinasclosetapi.category')),
            ],
        ),
        migrations.CreateModel(
            name='Retailer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('retailer_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_name', models.CharField(max_length=50)),
                ('note', models.CharField(max_length=250)),
                ('is_favorite', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserPiece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=50)),
                ('is_favorite', models.BooleanField(default=False)),
                ('look', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='alinasclosetapi.look')),
                ('piece', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alinasclosetapi.piece')),
                ('shopping_list', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='alinasclosetapi.shoppinglist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='piece',
            name='retailer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alinasclosetapi.retailer'),
        ),
    ]
