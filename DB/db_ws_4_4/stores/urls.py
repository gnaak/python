from django.urls import path
from . import views

app_name = 'stores'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:store_pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:store_pk>/product/', views.product, name='product'),
    path(
        '<int:store_pk>/comment/<int:product_pk>/delete', 
        views.comment_delete, name='comment_delete'),
]


