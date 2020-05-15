# Generated by Django 1.9.2 on 2016-02-01 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("djangocms_blog", "0012_auto_20151220_1734"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="categories",
            field=models.ManyToManyField(
                blank=True, related_name="blog_posts", to="djangocms_blog.BlogCategory", verbose_name="category"
            ),
        ),
    ]
