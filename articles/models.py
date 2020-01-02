from django.db import models


class Article(models.Model):
    url = models.URLField(null=False, blank=False)
    user = models.ForeignKey('auth.User', null=False, blank=True, on_delete=models.CASCADE)
    text = models.TextField(null=False, blank=False)
    polarity = models.CharField(null=False, blank=False, max_length=100)
    subjectivity = models.CharField(null=False, blank=False, max_length=100)
    polarity_confidence = models.DecimalField(null=False, blank=False, decimal_places=18, max_digits=20)
    subjectivity_confidence = models.DecimalField(null=False, blank=False, decimal_places=18, max_digits=20)
    language = models.CharField(null=False, blank=False, max_length=3)


class ArticleCategory(models.Model):
    article = models.ForeignKey('articles.Article', null=False, blank=True, related_name="categories", on_delete=models.CASCADE)
    label = models.CharField(null=False, blank=False, max_length=100)
    code = models.CharField(null=False, blank=False, max_length=10)
    confidence = models.IntegerField(null=False, blank=False)


class ArticleEntityGroup(models.Model):
    article = models.ForeignKey('articles.Article', null=False, blank=True, related_name="entities_group", on_delete=models.CASCADE)
    group = models.CharField(null=False, blank=False, max_length=100)


class ArticleEntity(models.Model):
    article_entity_group = models.ForeignKey('articles.ArticleEntityGroup', null=False, blank=True, related_name="entities", on_delete=models.CASCADE)
    entity = models.CharField(null=False, blank=False, max_length=100)


class ArticleConcept(models.Model):
    article = models.ForeignKey('articles.Article', null=False, blank=True, related_name="concept", on_delete=models.CASCADE)
    concept = models.URLField(null=False, blank=False)
    support = models.IntegerField(null=False, blank=False)


class ArticleConceptSurfaceForm(models.Model):
    article_concept = models.ForeignKey('articles.ArticleConcept', null=False, blank=True, related_name="surface_forms", on_delete=models.CASCADE)
    string = models.CharField(null=False, blank=False, max_length=100)
    score = models.IntegerField(null=False, blank=False)
    offset = models.IntegerField(null=False, blank=False)


class ArticleConceptType(models.Model):
    article_concept = models.ForeignKey('articles.ArticleConcept', null=False, blank=True, related_name="types", on_delete=models.CASCADE)
    type = models.URLField(null=False, blank=False)


class ArticleSummary(models.Model):
    article = models.ForeignKey('articles.Article', null=False, blank=True, related_name="summaries", on_delete=models.CASCADE)
    sentence = models.TextField(null=False, blank=False)
