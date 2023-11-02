from django.urls import path
from .views import HomePage, ArticleDetail, AddPostView, EditPostView, DeletePostView, AddCommentView
from . import views

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("article/<int:pk>", ArticleDetail.as_view(), name="article-detail"),
    path("post/", AddPostView.as_view(), name="add_post"),
    path("article/edit/<int:pk>", EditPostView.as_view(), name="edit_post"),
    path("article/<int:pk>/delete", DeletePostView.as_view(), name="delete_post"),
    path("article/<int:pk>/comment", AddCommentView.as_view(), name="add_comment"),
    path('search/', views.search_view, name='search'),
]
