# Generated by Django 2.1.1 on 2018-09-30 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_publicationhouse'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publicationhouse',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='library.PublicationHouse'),
        ),
    ]
