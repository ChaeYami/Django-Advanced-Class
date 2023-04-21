from django.urls import path, include
from articles import views


urlpatterns = [
    
    path("", views.articleAPI, name = "index"), # articles/index/
    path("<int:article_id>/", views.ArticleList.as_view(), name = "article_view"), # articles/id/ 
    
]
