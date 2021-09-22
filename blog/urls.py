from django.urls import path

from .views import PostApiView, PostDetailApiView, CategoryApiView, TagApiView, AuthorApiView

urlpatterns = [
    path('posts/', PostApiView.as_view()),
    path('post/<slug:slug>', PostDetailApiView.as_view()),
    path('categories/', CategoryApiView.as_view()),
    path('tags/', TagApiView.as_view()),
    path('authors/', AuthorApiView.as_view())
]