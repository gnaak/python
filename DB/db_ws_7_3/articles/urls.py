from django.urls import path
from . import views


urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('articles/comments/', views.comment_list),
    path('articles/comments/<int:comment_pk>/', views.comment_detail),
    path('articles/comments/<int:article_pk>/comments/', views.comment_create),
]
