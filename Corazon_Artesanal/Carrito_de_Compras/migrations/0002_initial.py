# Generated by Django 4.2.5 on 2023-11-19 20:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Carrito_de_Compras', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carritocompra',
            name='compradorID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
