from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from articles.models import Article
from articles.services import get_info_to_article
from articles.serializers import ArticleSerializer, ArticlesUploadSerializer


class ArticlesListAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        articles = Article.objects.filter(user=request.user).all()
        return Response(data=ArticleSerializer(articles, many=True).data)


class ArticlesUploadAPIView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticlesUploadSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        articles = get_info_to_article(request.data.get('url'), request.user)
        return Response(data=ArticleSerializer(articles).data)
