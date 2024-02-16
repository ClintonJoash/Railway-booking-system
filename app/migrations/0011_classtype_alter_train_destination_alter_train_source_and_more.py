# Generated by Django 4.0.2 on 2022-02-20 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_train_destination_alter_train_source'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='train',
            name='destination',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='To+', to='app.station'),
        ),
        migrations.AlterField(
            model_name='train',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='From+', to='app.station'),
        ),
        migrations.AddField(
            model_name='train',
            name='class_type',
            field=models.ManyToManyField(blank=True, null=True, to='app.ClassType'),
        ),
    ]
