# Generated by Django 4.1 on 2022-09-03 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_delete_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bad', models.BooleanField(default=False)),
                ('average', models.BooleanField(default=False)),
                ('good', models.BooleanField(default=False)),
                ('vgood', models.BooleanField(default=False)),
                ('excellent', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
            ],
        ),
    ]