# Generated by Django 4.1 on 2022-09-04 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_category_parent_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(blank=True, default=None, related_name='posts', to='blog.category'),
        ),
    ]
