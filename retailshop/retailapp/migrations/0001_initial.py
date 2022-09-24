# Generated by Django 4.1.1 on 2022-09-24 00:51

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
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('quantity', models.IntegerField(null=True)),
                ('date_and_time_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-product_name',),
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_quantity', models.IntegerField()),
                ('product_cost', models.FloatField(default=0.0)),
                ('date_of_ordering', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('delivered', 'Delivered')], default='pending', max_length=100)),
                ('product_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_product', to='retailapp.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
