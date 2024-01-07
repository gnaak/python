from django.urls import path
from . import views

app_name = 'eithers'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'), 
    path('random/', views.random, name='random'), 
    path('<int:pk>', views.detail, name='detail'), 
    path(
        '<int:pk>/comment/',
        views.comments_create,
        name='comments_create') 
    
]