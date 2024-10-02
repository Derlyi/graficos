# Generated by Django 5.1.1 on 2024-09-28 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promocion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descuento', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'promoción',
                'verbose_name_plural': 'promociones',
                'ordering': ['nombre'],
            },
        ),
    ]