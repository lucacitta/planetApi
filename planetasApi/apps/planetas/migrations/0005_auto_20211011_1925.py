# Generated by Django 3.2.8 on 2021-10-11 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planetas', '0004_auto_20211011_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdministradorMailApi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailAdministrador', models.EmailField(max_length=254)),
                ('emailEnvioCorreos', models.EmailField(max_length=254)),
                ('contraseñaMailEnvioCorreos', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Administrador',
                'verbose_name_plural': 'Administradores',
            },
        ),
        migrations.AlterField(
            model_name='planetasapi',
            name='img_geology',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='planetasapi',
            name='img_internal',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='planetasapi',
            name='img_planet',
            field=models.ImageField(upload_to='images'),
        ),
    ]
