from aylienapiclient import textapi
from aylienapiclient.errors import HttpError
from articles.models import Article, ArticleCategory, ArticleConcept, ArticleConceptSurfaceForm, ArticleConceptType, \
    ArticleEntity, ArticleEntityGroup, ArticleSummary
from django.db import transaction
from django.conf import settings

api_text_client = textapi.Client(settings.AYLIEN_API_APP_ID, settings.AYLIEN_API_APP_KEY)


def get_sentiment_to_article(article_url):
    try:
        article_sentiment = api_text_client.Sentiment({'url': article_url})
    except HttpError:
        raise ValueError('url is invalid or article not found')
    return article_sentiment


def get_classification_to_article(article_url):
    try:
        article_classification = api_text_client.Classify({'url': article_url})
    except HttpError:
        raise ValueError('url is invalid or article not found')
    return article_classification


def get_entities_to_article(article_url):
    try:
        article_entities = api_text_client.Entities({'url': article_url})
    except HttpError:
        raise ValueError('url is invalid or article not found')
    return article_entities


def get_concept_to_article(article_url):
    try:
        article_concept = api_text_client.Concepts({'url': article_url})
    except HttpError:
        raise ValueError('url is invalid or article not found')
    return article_concept


def get_summary_to_article(article_url):
    try:
        article_summary = api_text_client.Summarize({'url': article_url})
    except HttpError:
        raise ValueError('url is invalid or article not found')
    return article_summary


def get_info_to_article(article_url, user):
    try:
        article_sentiment_info = get_sentiment_to_article(article_url)
        article_classification_info = get_classification_to_article(article_url)
        article_entities_info = get_entities_to_article(article_url)
        article_concept_info = get_concept_to_article(article_url)
        article_summary_info = get_summary_to_article(article_url)
    except ValueError:
        raise ValueError('url is invalid or article not found')

    with transaction.atomic() as atomic:
        article = Article.objects.create(
            user=user,
            text=article_sentiment_info.get('text'),
            polarity=article_sentiment_info.get('polarity'),
            subjectivity=article_sentiment_info.get('subjectivity'),
            polarity_confidence=article_sentiment_info.get('polarity_confidence'),
            subjectivity_confidence=article_sentiment_info.get('subjectivity_confidence'),
            language=article_classification_info.get('language'),
        )

        article_categories = [ArticleCategory(
            article=article,
            label=category.get("label"),
            code=category.get("code"),
            confidence=category.get("confidence"),
        ) for category in article_classification_info.get('categories')]

        ArticleCategory.objects.bulk_create(article_categories)

        for entities_group, entities in article_entities_info.get('entities').items():
            article_entity_group = ArticleEntityGroup.objects.create(
                article=article,
                group=entities_group,
            )

            article_entities = [ArticleEntity(
                article_entity_group=article_entity_group,
                entity=entity
            ) for entity in entities]

            ArticleEntity.objects.bulk_create(article_entities)

        for concept, concept_info in article_concept_info.get('concepts').items():
            article_concept = ArticleConcept.objects.create(
                article=article,
                concept=concept,
                support=concept_info.get('support'),
            )

            article_concept_surface_forms = [ArticleConceptSurfaceForm(
                article_concept=article_concept,
                string=surface_form.get('string'),
                score=surface_form.get('score'),
                offset=surface_form.get('offset'),
            ) for surface_form in concept_info.get('surfaceForms')]

            ArticleConceptSurfaceForm.objects.bulk_create(article_concept_surface_forms)

            article_concept_types = [ArticleConceptType(
                article_concept=article_concept,
                type=type,
            ) for type in concept_info.get('types')]

            ArticleConceptType.objects.bulk_create(article_concept_types)

        article_summaries = [ArticleSummary(
            article=article,
            sentence=sentence,
        ) for sentence in article_summary_info.get('sentences')]

        ArticleSummary.objects.bulk_create(article_summaries)

    return article
