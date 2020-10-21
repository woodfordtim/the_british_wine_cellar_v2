# Generated by Django 3.1.2 on 2020-10-21 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20201021_2235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wine_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='wine',
            name='wine_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.wine_type'),
        ),
    ]
