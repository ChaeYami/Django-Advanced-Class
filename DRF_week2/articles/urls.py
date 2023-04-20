from django.urls import path, include
from articles import views

urlpatterns = [
    
    path("", views.articleAPI, name = "index"), # articles/index/
    path("<int:article_id>/", views.articleDetailAPI, name = "article_view"), # articles/id/ 
    
]