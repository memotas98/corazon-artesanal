from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name = 'InformacionPrivada',
            fields=[
                ('id_artesano', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_informacion_publica', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('contrasena', models.TextField())
            ],
        ),
    ]