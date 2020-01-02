# Generated by Django 3.0.1 on 2020-01-02 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20200101_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecategory',
            name='article',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='articles.Article'),
        ),
        migrations.AlterField(
            model_name='articleconcept',
            name='article',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='concept', to='articles.Article'),
        ),
        migrations.AlterField(
            model_name='articleconceptsurfaceform',
            name='article_concept',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='surface_forms', to='articles.ArticleConcept'),
        ),
        migrations.AlterField(
            model_name='articleconcepttype',
            name='article_concept',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='types', to='articles.ArticleConcept'),
        ),
        migrations.AlterField(
            model_name='articleentity',
            name='article_entity_group',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='entities', to='articles.ArticleEntityGroup'),
        ),
        migrations.AlterField(
            model_name='articleentitygroup',
            name='article',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='entities_group', to='articles.Article'),
        ),
        migrations.AlterField(
            model_name='articlesummary',
            name='article',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='summaries', to='articles.Article'),
        ),
    ]