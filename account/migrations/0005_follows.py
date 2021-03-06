# Generated by Django 4.0.3 on 2022-03-09 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='account.profile')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='account.profile')),
            ],
        ),
    ]
