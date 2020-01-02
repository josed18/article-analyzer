from rest_framework import serializers
from articles.models import Article, ArticleCategory, ArticleEntityGroup, ArticleEntity, ArticleConcept, \
    ArticleConceptSurfaceForm, ArticleConceptType, ArticleSummary


class ArticleSummarySerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleSummary
        fields = ('sentence', )


class ArticleConceptTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleConceptType
        fields = ('type', )


class ArticleConceptSurfaceFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleConceptSurfaceForm
        fields = ('string', 'score', 'offset')


class ArticleConceptSerializer(serializers.ModelSerializer):
    surface_forms = serializers.SerializerMethodField()
    types = serializers.SerializerMethodField()

    class Meta:
        model = ArticleConcept
        fields = ('concept', 'support', 'surface_forms', 'types')

    def get_surface_forms(self, obj):
        return ArticleConceptSurfaceFormSerializer(obj.surface_forms.all(), many=True).data

    def get_types(self, obj):
        return ArticleConceptTypeSerializer(obj.types.all(), many=True).data


class ArticleEntitySerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleEntity
        fields = ('entity', )


class ArticleEntityGroupSerializer(serializers.ModelSerializer):
    entities = serializers.SerializerMethodField()

    class Meta:
        model = ArticleEntityGroup
        fields = ('group', 'entities')

    def get_entities(self, obj):
        return ArticleEntitySerializer(obj.entities.all(), many=True).data


class ArticleCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleCategory
        fields = ('label', 'code', 'confidence')


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    categories = serializers.SerializerMethodField()
    entities_group = serializers.SerializerMethodField()
    concept = serializers.SerializerMethodField()
    summaries = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ('id', 'user', 'url', 'text', 'polarity', 'subjectivity', 'polarity_confidence', 'subjectivity_confidence',
                  'language', 'categories', 'entities_group', 'concept', 'summaries')

    def get_user(self, obj):
        if obj.user is None:
            return None
        return obj.user.username

    def get_categories(self, obj):
        return ArticleCategorySerializer(obj.categories.all(), many=True).data

    def get_entities_group(self, obj):
        return ArticleEntityGroupSerializer(obj.entities_group.all(), many=True).data

    def get_concept(self, obj):
        return ArticleConceptSerializer(obj.concept.all(), many=True).data

    def get_summaries(self, obj):
        return ArticleSummarySerializer(obj.summaries.all(), many=True).data


class ArticlesUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('url', )
