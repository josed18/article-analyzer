from django.conf.urls import url, include
from articles.views import ArticlesListAPIView, ArticlesUploadAPIView

urlpatterns = [
    url(r'^$', ArticlesListAPIView.as_view()),
    url(r'^upload/$', ArticlesUploadAPIView.as_view()),
]