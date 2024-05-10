from django.urls import path

from . import views

urlpatterns = [
    path('fetchArticles/<str:category>/',views.fetchArticles,name="fetch-articles"),
	path('fetchArticleByNews/<str:websiteName>/',views.fetchArticleByNews,name="fetch-articles"),
	path('translate/',views.translator,name="translate"),
    path('recommendation/',views.recommendation,name="recommendation"),
    path('summarize/',views.articleSummarizer,name="summarize"),
    path('search/',views.searchArticles,name="search"),
    path('api/register/', views.RegisterAPI.as_view(), name='register'),
    path('api/login/', views.LoginAPI.as_view(), name='login'),

    path('scrape/',views.SCRAPE,name="scrape")
]
