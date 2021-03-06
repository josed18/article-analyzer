# Generated by Django 3.0.1 on 2020-01-01 21:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('text', models.TextField()),
                ('polarity', models.CharField(max_length=100)),
                ('subjectivity', models.CharField(max_length=100)),
                ('polarity_confidence', models.DecimalField(decimal_places=18, max_digits=20)),
                ('subjectivity_confidence', models.DecimalField(decimal_places=18, max_digits=20)),
                ('language', models.CharField(max_length=3)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleConcept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concept', models.URLField()),
                ('support', models.IntegerField()),
                ('article', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentences', models.TextField()),
                ('article', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleEntityGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('article', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity', models.CharField(max_length=100)),
                ('article_entity_group', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='articles.ArticleEntityGroup')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleConceptType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.URLField()),
                ('article_concept', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='articles.ArticleConcept')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleConceptSurfaceForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('string', models.CharField(max_length=100)),
                ('score', models.IntegerField()),
                ('offset', models.IntegerField()),
                ('article_concept', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='articles.ArticleConcept')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10)),
                ('article', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
            ],
        ),
    ]
