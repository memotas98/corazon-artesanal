# Generated by Django 4.2.5 on 2023-11-19 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Gestion_de_Inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarritoCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCarrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('CarritoID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Carrito_de_Compras.carritocompra')),
                ('obraID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion_de_Inventario.obra')),
            ],
        ),
    ]
