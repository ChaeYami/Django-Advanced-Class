from django.urls import path
from articles import views


urlpatterns = [
    path("/", views.ArticleView.as_view(), name="article_view"),
    path(
        "<int:article_id>/",
        views.ArticleDetailView.as_view(),
        name="article_detail_view",
    ),
    path("comment/", views.CommentView.as_view(), name="comment_view"),
    path(
        "comment/<int:comment_id>",
        views.CommentDetailView.as_view(),
        name="comment_detail_view",
    ),
    path("like/", views.LikeView.as_view(), name="like_view"),
]
"""
-- 댓글 url에 대해서 --
<int:article_id>/comment 로 url을 지정하고, view에서 매개변수로 받게 함으로써 해당 글의 댓글을 불러올 수도 있다.
이 강의에서는 그렇게 하진 않고 comment를 보낼 때 body 안에 article_id 를 실어서 보내도록 한다. (url이 깔끔하라고)
- 좋아요도 같은 맥락
"""
